package decaf.error;

import decaf.Location;

/**
 * example：unrecognized char: '@'<br>
 * PA1
 */
public class MulCommentUnclosedError extends DecafError {

	public MulCommentUnclosedError(Location location) {
		super(location);
	}

	@Override
	protected String getErrMsg() {
		return "unterminated multi comment";
	}
}
