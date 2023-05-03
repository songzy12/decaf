package decaf.dataflow;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeSet;
import java.util.HashSet;

import decaf.machdesc.Asm;
import decaf.machdesc.Register;
import decaf.tac.Label;
import decaf.tac.Tac;
import decaf.tac.Temp;

public class BasicBlock {
	public int bbNum;

	public enum EndKind {
		BY_BRANCH, BY_BEQZ, BY_BNEZ, BY_RETURN
	}

	public EndKind endKind;

	public int inDegree;

	public Tac tacList;

	public Label label;

	public Temp var;
	
	public Tac varTac;

	public Register varReg;

	public int[] next;

	public boolean cancelled;

	public boolean mark;

	public Set<Temp> def;
	public Set<Temp> liveUse;
	public Set<Temp> liveIn;
	public Set<Temp> liveOut;
	public HashMap<Tac, Temp> liveUseExt;
	public HashMap<Tac, Temp> liveInExt;
	public HashMap<Tac, Temp> liveOutExt;
	
	public Set<Temp> saves;

	private List<Asm> asms;

	public BasicBlock() {
		def = new TreeSet<Temp>(Temp.ID_COMPARATOR);
		liveUse = new TreeSet<Temp>(Temp.ID_COMPARATOR);
		liveIn = new TreeSet<Temp>(Temp.ID_COMPARATOR);
		liveOut = new TreeSet<Temp>(Temp.ID_COMPARATOR);
		liveUseExt = new HashMap<Tac, Temp>();
		liveInExt = new HashMap<Tac, Temp>();
		liveOutExt = new HashMap<Tac, Temp>();
		next = new int[2];
		asms = new ArrayList<Asm>();
	}

	public void computeDefAndLiveUse() {
		for (Tac tac = tacList; tac != null; tac = tac.next) {
			switch (tac.opc) {
			case ADD:
			case SUB:
			case MUL:
			case DIV:
			case MOD:
			case LAND:
			case LOR:
			case GTR:
			case GEQ:
			case EQU:
			case NEQ:
			case LEQ:
			case LES:
				/* use op1 and op2, def op0 */
				if (tac.op1.lastVisitedBB != bbNum) {
					liveUse.add (tac.op1);
					liveUseExt.put(tac, tac.op1);
					tac.op1.lastVisitedBB = bbNum;
				}
				if (tac.op2.lastVisitedBB != bbNum) {
					liveUse.add (tac.op2);
					liveUseExt.put(tac, tac.op2);
					tac.op2.lastVisitedBB = bbNum;
				}
				if (tac.op0.lastVisitedBB != bbNum) {
					def.add (tac.op0);
					tac.op0.lastVisitedBB = bbNum;
				}
				break;
			case NEG:
			case LNOT:
			case ASSIGN:
			case INDIRECT_CALL:
			case LOAD:
				/* use op1, def op0 */
				if (tac.op1.lastVisitedBB != bbNum) {
					liveUse.add (tac.op1);
					liveUseExt.put(tac, tac.op1);
					tac.op1.lastVisitedBB = bbNum;
				}
				if (tac.op0 != null && tac.op0.lastVisitedBB != bbNum) {  // in INDIRECT_CALL with return type VOID,
					// tac.op0 is null
					def.add (tac.op0);
					tac.op0.lastVisitedBB = bbNum;
				}
				break;
			case LOAD_VTBL:
			case DIRECT_CALL:
			case RETURN:
			case LOAD_STR_CONST:
			case LOAD_IMM4:
				/* def op0 */
				if (tac.op0 != null && tac.op0.lastVisitedBB != bbNum) {  // in DIRECT_CALL with return type VOID,
					// tac.op0 is null
					def.add (tac.op0);
					tac.op0.lastVisitedBB = bbNum;
				}
				break;
			case STORE:
				/* use op0 and op1*/
				if (tac.op0.lastVisitedBB != bbNum) {
					liveUse.add (tac.op0);
					liveUseExt.put(tac, tac.op0);
					tac.op0.lastVisitedBB = bbNum;
				}
				if (tac.op1.lastVisitedBB != bbNum) {
					liveUse.add (tac.op1);
					liveUseExt.put(tac, tac.op1);
					tac.op1.lastVisitedBB = bbNum;
				}
				break;
			case PARM:
				/* use op0 */
				if (tac.op0.lastVisitedBB != bbNum) {
					liveUse.add (tac.op0);
					liveUseExt.put(tac, tac.op0);
					tac.op0.lastVisitedBB = bbNum;
				}
				break;
			default:
				/* BRANCH MEMO MARK PARM*/
				break;
			}
		}
		if (var != null && var.lastVisitedBB != bbNum) {
			liveUse.add (var);
			liveUseExt.put(varTac, var);
			var.lastVisitedBB = bbNum;
		}
		liveIn.addAll (liveUse);
		Iterator<Entry<Tac, Temp>> iterator = liveUseExt.entrySet().iterator();   
		while (iterator.hasNext()){   
			Entry<Tac, Temp> entry = iterator.next();
			if (!liveInExt.containsKey(entry.getKey()))
				liveInExt.put(entry.getKey(), entry.getValue());
		}
	}

	public void analyzeLiveness() {
		if (tacList == null)
			return;
		Tac tac = tacList;
		for (; tac.next != null; tac = tac.next);

		tac.liveOut = new HashSet<Temp> (liveOut);
		if (var != null)
			tac.liveOut.add (var);
		for (; tac != tacList; tac = tac.prev) {
			tac.prev.liveOut = new HashSet<Temp> (tac.liveOut);
			switch (tac.opc) {
			case ADD:
			case SUB:
			case MUL:
			case DIV:
			case MOD:
			case LAND:
			case LOR:
			case GTR:
			case GEQ:
			case EQU:
			case NEQ:
			case LEQ:
			case LES:
				/* use op1 and op2, def op0 */
				tac.prev.liveOut.remove (tac.op0);
				tac.prev.liveOut.add (tac.op1);
				tac.prev.liveOut.add (tac.op2);
				break;
			case NEG:
			case LNOT:
			case ASSIGN:
			case INDIRECT_CALL:
			case LOAD:
				/* use op1, def op0 */
				tac.prev.liveOut.remove (tac.op0);
				tac.prev.liveOut.add (tac.op1);
				break;
			case LOAD_VTBL:
			case DIRECT_CALL:
			case RETURN:
			case LOAD_STR_CONST:
			case LOAD_IMM4:
				/* def op0 */
				tac.prev.liveOut.remove (tac.op0);
				break;
			case STORE:
				/* use op0 and op1*/
				tac.prev.liveOut.add (tac.op0);
				tac.prev.liveOut.add (tac.op1);
				break;
			case BEQZ:
			case BNEZ:
			case PARM:
				/* use op0 */
				tac.prev.liveOut.add (tac.op0);
				break;
			default:
				/* BRANCH MEMO MARK PARM*/
				break;
			}
		}
	}

	public void analyzeDUChain() {
		for (Tac tl = tacList; tl != null; tl = tl.next) {
			tl.du = new TreeSet<Tac>(Tac.COMPARATOR);
			Temp temp = tempDefined(tl);
			if (temp != null) {
				Tac tl2;
				for (tl2 = tl.next; tl2 != null; tl2 = tl2.next) {
					if (tempUsed(tl2, temp))
						tl.du.add(tl2);
					
					Temp temp2 = tempDefined(tl2);
					if (temp == temp2)
						break;
				}
			
				if (tl2 == null){
					Iterator<Entry<Tac, Temp>> iterator = liveOutExt.entrySet().iterator();   
					while (iterator.hasNext()){   
						Entry<Tac, Temp> entry = iterator.next();
						if (tempUsed(entry.getKey(), temp))
							tl.du.add(entry.getKey());
					}   
				}
			}
		}
	}
	
	private boolean tempUsed(Tac tac, Temp temp){
		switch(tac.opc){
			case ADD:
			case SUB:
			case MUL:
			case DIV:
			case MOD:
			case LAND:
			case LOR:
			case GTR:
			case GEQ:
			case EQU:
			case NEQ:
			case LEQ:
			case LES:
				return ( temp == tac.op1 || temp == tac.op2);
			case NEG:
			case LNOT:
			case ASSIGN:
			case INDIRECT_CALL:
			case LOAD:
				return (temp == tac.op1);
			case STORE:
				return (temp == tac.op0 || temp == tac.op1);
			case BEQZ:
			case BNEZ:
			case PARM:
				return (temp == tac.op0);
			case LOAD_VTBL:
			case DIRECT_CALL:
			case RETURN:
			case LOAD_STR_CONST:
			case LOAD_IMM4:
			default:
				return false;
		}
	}

	private Temp tempDefined(Tac tac) {
		switch (tac.opc) {
			case ADD:
			case SUB:
			case MUL:
			case DIV:
			case MOD:
			case LAND:
			case LOR:
			case GTR:
			case GEQ:
			case EQU:
			case NEQ:
			case LEQ:
			case LES:
			case NEG:
			case LNOT:
			case ASSIGN:
			case INDIRECT_CALL:
			case LOAD:
			case LOAD_VTBL:
			case DIRECT_CALL:
			case RETURN:
			case LOAD_STR_CONST:
			case LOAD_IMM4:
				return tac.op0;
			default:
				return null;
		}
	}

	public void dispatchId() {
		int id = 0;
		for (Tac t = tacList; t != null; t = t.next)
			t.id = ++id;
	}

	public void printLivenessTo(PrintWriter pw) {
		pw.println("BASIC BLOCK " + bbNum + " : ");
		pw.println("  Def     = " + toString(def));
		pw.println("  liveUse = " + toString(liveUse));
		pw.println("  liveIn  = " + toString(liveIn));
		pw.println("  liveOut = " + toString(liveOut));

		for (Tac t = tacList; t != null; t = t.next) {
			pw.println("    " + t + " " + toString(t.liveOut));
		}

		switch (endKind) {
		case BY_BRANCH:
			pw.println("END BY BRANCH, goto " + next[0]);
			break;
		case BY_BEQZ:
			pw.println("END BY BEQZ, if " + var.name + " = ");
			pw.println("    0 : goto " + next[0] + "; 1 : goto " + next[1]);
			break;
		case BY_BNEZ:
			pw.println("END BY BGTZ, if " + var.name + " = ");
			pw.println("    1 : goto " + next[0] + "; 0 : goto " + next[1]);
			break;
		case BY_RETURN:
			if (var != null) {
				pw.println("END BY RETURN, result = " + var.name);
			} else {
				pw.println("END BY RETURN, void result");
			}
			break;
		}
	}
	
	public void printDUTo(PrintWriter pw) {
		pw.println("BASIC BLOCK " + bbNum + " : ");
		pw.println("  Def     = " + toString(def));
		pw.println("  liveUse = " + toString(liveUse));
		pw.println("  liveIn  = " + toString(liveIn));
		pw.println("  liveOut = " + toString(liveOut));

		for (Tac t = tacList; t != null; t = t.next) {
			pw.println("    " + t + " " + DUToString(t.du));
		}

		switch (endKind) {
		case BY_BRANCH:
			pw.println("END BY BRANCH, goto " + next[0]);
			break;
		case BY_BEQZ:
			pw.println("END BY BEQZ, if " + var.name + " = ");
			pw.println("    0 : goto " + next[0] + "; 1 : goto " + next[1]);
			break;
		case BY_BNEZ:
			pw.println("END BY BGTZ, if " + var.name + " = ");
			pw.println("    1 : goto " + next[0] + "; 0 : goto " + next[1]);
			break;
		case BY_RETURN:
			if (var != null) {
				pw.println("END BY RETURN, result = " + var.name);
			} else {
				pw.println("END BY RETURN, void result");
			}
			break;
		}
	}

	public String toString(Set<Temp> set) {
		StringBuilder sb = new StringBuilder("[ ");
		for (Temp t : set) {
			sb.append(t.name + " ");
		}
		sb.append(']');
		return sb.toString();
	}

	public String DUToString(Set<Tac> set) {
		StringBuilder sb = new StringBuilder("[ ");
		for (Tac t : set) {
			// b means block, t means tac
			sb.append("(b"+t.bbNum + ", t" + t.id + ") ");
		}
		sb.append("]");
		return sb.toString();
	}

	public void insertBefore(Tac insert, Tac base) {
		if (base == tacList) {
			tacList = insert;
		} else {
			base.prev.next = insert;
		}
		insert.prev = base.prev;
		base.prev = insert;
		insert.next = base;
	}

	public void insertAfter(Tac insert, Tac base) {
		if (tacList == null) {
			tacList = insert;
			insert.next = null;
			return;
		}
		if (base.next != null) {
			base.next.prev = insert;
		}
		insert.prev = base;
		insert.next = base.next;
		base.next = insert;
	}

	public void appendAsm(Asm asm) {
		asms.add(asm);
	}

	public List<Asm> getAsms() {
		return asms;
	}
}
