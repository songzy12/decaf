VTABLE(_rndModule) {
    rndModule
    _rndModule.Init;
    _rndModule.Random;
    _rndModule.RndInt;
}

VTABLE(_Deck) {
    Deck
    _Deck.Init;
    _Deck.Shuffle;
    _Deck.GetCard;
}

VTABLE(_BJDeck) {
    BJDeck
    _BJDeck.Init;
    _BJDeck.DealCard;
    _BJDeck.Shuffle;
    _BJDeck.NumCardsRemaining;
}

VTABLE(_Player) {
    Player
    _Player.Init;
    _Player.Hit;
    _Player.DoubleDown;
    _Player.TakeTurn;
    _Player.HasMoney;
    _Player.PrintMoney;
    _Player.PlaceBet;
    _Player.GetTotal;
    _Player.Resolve;
    _Player.GetYesOrNo;
}

VTABLE(_Dealer) {
    Dealer
    _Dealer.Init;
    _Player.Hit;
    _Player.DoubleDown;
    _Dealer.TakeTurn;
    _Player.HasMoney;
    _Player.PrintMoney;
    _Player.PlaceBet;
    _Player.GetTotal;
    _Player.Resolve;
    _Player.GetYesOrNo;
}

VTABLE(_House) {
    House
    _House.SetupGame;
    _House.SetupPlayers;
    _House.TakeAllBets;
    _House.TakeAllTurns;
    _House.ResolveAllPlayers;
    _House.PrintAllMoney;
    _House.PlayOneGame;
}

VTABLE(_Main) {
    Main
}

FUNCTION(_rndModule_New) {
memo ''
_rndModule_New:
    _T42 = 8
    parm _T42
    _T43 =  call _Alloc
    _T44 = 0
    *(_T43 + 4) = _T44
    _T45 = VTBL <_rndModule>
    *(_T43 + 0) = _T45
    return _T43
}

FUNCTION(_Deck_New) {
memo ''
_Deck_New:
    _T46 = 16
    parm _T46
    _T47 =  call _Alloc
    _T48 = 0
    *(_T47 + 4) = _T48
    *(_T47 + 8) = _T48
    *(_T47 + 12) = _T48
    _T49 = VTBL <_Deck>
    *(_T47 + 0) = _T49
    return _T47
}

FUNCTION(_BJDeck_New) {
memo ''
_BJDeck_New:
    _T50 = 16
    parm _T50
    _T51 =  call _Alloc
    _T52 = 0
    *(_T51 + 4) = _T52
    *(_T51 + 8) = _T52
    *(_T51 + 12) = _T52
    _T53 = VTBL <_BJDeck>
    *(_T51 + 0) = _T53
    return _T51
}

FUNCTION(_Player_New) {
memo ''
_Player_New:
    _T54 = 28
    parm _T54
    _T55 =  call _Alloc
    _T56 = 0
    _T57 = 4
    _T58 = (_T55 + _T54)
_L43:
    _T59 = (_T58 - _T57)
    _T58 = _T59
    _T60 = (_T54 - _T57)
    _T54 = _T60
    if (_T54 == 0) branch _L44
    *(_T58 + 0) = _T56
    branch _L43
_L44:
    _T61 = VTBL <_Player>
    *(_T58 + 0) = _T61
    return _T58
}

FUNCTION(_Dealer_New) {
memo ''
_Dealer_New:
    _T62 = 28
    parm _T62
    _T63 =  call _Alloc
    _T64 = 0
    _T65 = 4
    _T66 = (_T63 + _T62)
_L46:
    _T67 = (_T66 - _T65)
    _T66 = _T67
    _T68 = (_T62 - _T65)
    _T62 = _T68
    if (_T62 == 0) branch _L47
    *(_T66 + 0) = _T64
    branch _L46
_L47:
    _T69 = VTBL <_Dealer>
    *(_T66 + 0) = _T69
    return _T66
}

FUNCTION(_House_New) {
memo ''
_House_New:
    _T70 = 16
    parm _T70
    _T71 =  call _Alloc
    _T72 = 0
    *(_T71 + 4) = _T72
    *(_T71 + 8) = _T72
    *(_T71 + 12) = _T72
    _T73 = VTBL <_House>
    *(_T71 + 0) = _T73
    return _T71
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T74 = 4
    parm _T74
    _T75 =  call _Alloc
    _T76 = VTBL <_Main>
    *(_T75 + 0) = _T76
    return _T75
}

FUNCTION(_rndModule.Init) {
memo '_T0:4 _T1:8'
_rndModule.Init:
    _T77 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_rndModule.Random) {
memo '_T2:4'
_rndModule.Random:
    _T78 = *(_T2 + 4)
    _T79 = 15625
    _T80 = *(_T2 + 4)
    _T81 = 10000
    _T82 = (_T80 % _T81)
    _T83 = (_T79 * _T82)
    _T84 = 22221
    _T85 = (_T83 + _T84)
    _T86 = 65536
    _T87 = (_T85 % _T86)
    *(_T2 + 4) = _T87
    _T88 = *(_T2 + 4)
    return _T88
}

FUNCTION(_rndModule.RndInt) {
memo '_T3:4 _T4:8'
_rndModule.RndInt:
    parm _T3
    _T89 = *(_T3 + 0)
    _T90 = *(_T89 + 12)
    _T91 =  call _T90
    _T92 = (_T91 % _T4)
    return _T92
}

FUNCTION(_Deck.Init) {
memo '_T5:4 _T6:8'
_Deck.Init:
    _T93 = *(_T5 + 8)
    _T94 = 52
    _T95 = 0
    _T96 = (_T94 < _T95)
    if (_T96 == 0) branch _L50
    _T97 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T97
    call _PrintString
    call _Halt
_L50:
    _T98 = 4
    _T99 = (_T98 * _T94)
    _T100 = (_T98 + _T99)
    parm _T100
    _T101 =  call _Alloc
    *(_T101 + 0) = _T94
    _T102 = 0
    _T101 = (_T101 + _T100)
_L51:
    _T100 = (_T100 - _T98)
    if (_T100 == 0) branch _L52
    _T101 = (_T101 - _T98)
    *(_T101 + 0) = _T102
    branch _L51
_L52:
    *(_T5 + 8) = _T101
    _T103 = *(_T5 + 12)
    *(_T5 + 12) = _T6
}

FUNCTION(_Deck.Shuffle) {
memo '_T7:4'
_Deck.Shuffle:
    _T104 = *(_T7 + 4)
    _T105 = 1
    *(_T7 + 4) = _T105
    branch _L53
_L54:
    _T106 = *(_T7 + 4)
    _T107 = *(_T7 + 4)
    _T108 = 1
    _T109 = (_T107 + _T108)
    *(_T7 + 4) = _T109
_L53:
    _T110 = *(_T7 + 4)
    _T111 = 52
    _T112 = (_T110 <= _T111)
    if (_T112 == 0) branch _L55
    _T113 = *(_T7 + 8)
    _T114 = *(_T7 + 4)
    _T115 = 1
    _T116 = (_T114 - _T115)
    _T117 = *(_T113 - 4)
    _T118 = (_T116 < _T117)
    if (_T118 == 0) branch _L56
    _T119 = 0
    _T120 = (_T116 < _T119)
    if (_T120 == 0) branch _L57
_L56:
    _T121 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T121
    call _PrintString
    call _Halt
_L57:
    _T122 = 4
    _T123 = (_T116 * _T122)
    _T124 = (_T113 + _T123)
    _T125 = *(_T124 + 0)
    _T126 = *(_T7 + 4)
    _T127 = 13
    _T128 = (_T126 % _T127)
    _T129 = 4
    _T130 = (_T116 * _T129)
    _T131 = (_T113 + _T130)
    *(_T131 + 0) = _T128
    branch _L54
_L55:
    _T132 = *(_T7 + 4)
    _T133 = *(_T7 + 4)
    _T134 = 1
    _T135 = (_T133 - _T134)
    *(_T7 + 4) = _T135
_L58:
    _T136 = *(_T7 + 4)
    _T137 = 0
    _T138 = (_T136 > _T137)
    if (_T138 == 0) branch _L59
    _T141 = *(_T7 + 12)
    _T142 = *(_T7 + 4)
    parm _T141
    parm _T142
    _T143 = *(_T141 + 0)
    _T144 = *(_T143 + 16)
    _T145 =  call _T144
    _T139 = _T145
    _T146 = *(_T7 + 4)
    _T147 = *(_T7 + 4)
    _T148 = 1
    _T149 = (_T147 - _T148)
    *(_T7 + 4) = _T149
    _T150 = *(_T7 + 8)
    _T151 = *(_T7 + 4)
    _T152 = *(_T150 - 4)
    _T153 = (_T151 < _T152)
    if (_T153 == 0) branch _L60
    _T154 = 0
    _T155 = (_T151 < _T154)
    if (_T155 == 0) branch _L61
_L60:
    _T156 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T156
    call _PrintString
    call _Halt
_L61:
    _T157 = 4
    _T158 = (_T151 * _T157)
    _T159 = (_T150 + _T158)
    _T160 = *(_T159 + 0)
    _T140 = _T160
    _T161 = *(_T7 + 8)
    _T162 = *(_T7 + 4)
    _T163 = *(_T161 - 4)
    _T164 = (_T162 < _T163)
    if (_T164 == 0) branch _L62
    _T165 = 0
    _T166 = (_T162 < _T165)
    if (_T166 == 0) branch _L63
_L62:
    _T167 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T167
    call _PrintString
    call _Halt
_L63:
    _T168 = 4
    _T169 = (_T162 * _T168)
    _T170 = (_T161 + _T169)
    _T171 = *(_T170 + 0)
    _T172 = *(_T7 + 8)
    _T173 = *(_T172 - 4)
    _T174 = (_T139 < _T173)
    if (_T174 == 0) branch _L64
    _T175 = 0
    _T176 = (_T139 < _T175)
    if (_T176 == 0) branch _L65
_L64:
    _T177 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T177
    call _PrintString
    call _Halt
_L65:
    _T178 = 4
    _T179 = (_T139 * _T178)
    _T180 = (_T172 + _T179)
    _T181 = *(_T180 + 0)
    _T182 = 4
    _T183 = (_T162 * _T182)
    _T184 = (_T161 + _T183)
    *(_T184 + 0) = _T181
    _T185 = *(_T7 + 8)
    _T186 = *(_T185 - 4)
    _T187 = (_T139 < _T186)
    if (_T187 == 0) branch _L66
    _T188 = 0
    _T189 = (_T139 < _T188)
    if (_T189 == 0) branch _L67
_L66:
    _T190 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T190
    call _PrintString
    call _Halt
_L67:
    _T191 = 4
    _T192 = (_T139 * _T191)
    _T193 = (_T185 + _T192)
    _T194 = *(_T193 + 0)
    _T195 = 4
    _T196 = (_T139 * _T195)
    _T197 = (_T185 + _T196)
    *(_T197 + 0) = _T140
    branch _L58
_L59:
}

FUNCTION(_Deck.GetCard) {
memo '_T8:4'
_Deck.GetCard:
    _T199 = *(_T8 + 4)
    _T200 = 52
    _T201 = (_T199 >= _T200)
    if (_T201 == 0) branch _L68
    _T202 = 0
    return _T202
_L68:
    _T203 = *(_T8 + 8)
    _T204 = *(_T8 + 4)
    _T205 = *(_T203 - 4)
    _T206 = (_T204 < _T205)
    if (_T206 == 0) branch _L69
    _T207 = 0
    _T208 = (_T204 < _T207)
    if (_T208 == 0) branch _L70
_L69:
    _T209 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T209
    call _PrintString
    call _Halt
_L70:
    _T210 = 4
    _T211 = (_T204 * _T210)
    _T212 = (_T203 + _T211)
    _T213 = *(_T212 + 0)
    _T198 = _T213
    _T214 = *(_T8 + 4)
    _T215 = *(_T8 + 4)
    _T216 = 1
    _T217 = (_T215 + _T216)
    *(_T8 + 4) = _T217
    return _T198
}

FUNCTION(_BJDeck.Init) {
memo '_T9:4 _T10:8'
_BJDeck.Init:
    _T219 = *(_T9 + 4)
    _T220 = 8
    _T221 = 0
    _T222 = (_T220 < _T221)
    if (_T222 == 0) branch _L71
    _T223 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T223
    call _PrintString
    call _Halt
_L71:
    _T224 = 4
    _T225 = (_T224 * _T220)
    _T226 = (_T224 + _T225)
    parm _T226
    _T227 =  call _Alloc
    *(_T227 + 0) = _T220
    _T228 = 0
    _T227 = (_T227 + _T226)
_L72:
    _T226 = (_T226 - _T224)
    if (_T226 == 0) branch _L73
    _T227 = (_T227 - _T224)
    *(_T227 + 0) = _T228
    branch _L72
_L73:
    *(_T9 + 4) = _T227
    _T229 = 0
    _T218 = _T229
    branch _L74
_L75:
    _T230 = 1
    _T231 = (_T218 + _T230)
    _T218 = _T231
_L74:
    _T232 = 8
    _T233 = (_T218 < _T232)
    if (_T233 == 0) branch _L76
    _T234 = *(_T9 + 4)
    _T235 = *(_T234 - 4)
    _T236 = (_T218 < _T235)
    if (_T236 == 0) branch _L77
    _T237 = 0
    _T238 = (_T218 < _T237)
    if (_T238 == 0) branch _L78
_L77:
    _T239 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T239
    call _PrintString
    call _Halt
_L78:
    _T240 = 4
    _T241 = (_T218 * _T240)
    _T242 = (_T234 + _T241)
    _T243 = *(_T242 + 0)
    _T244 =  call _Deck_New
    _T245 = 4
    _T246 = (_T218 * _T245)
    _T247 = (_T234 + _T246)
    *(_T247 + 0) = _T244
    _T248 = *(_T9 + 4)
    _T249 = *(_T248 - 4)
    _T250 = (_T218 < _T249)
    if (_T250 == 0) branch _L79
    _T251 = 0
    _T252 = (_T218 < _T251)
    if (_T252 == 0) branch _L80
_L79:
    _T253 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T253
    call _PrintString
    call _Halt
_L80:
    _T254 = 4
    _T255 = (_T218 * _T254)
    _T256 = (_T248 + _T255)
    _T257 = *(_T256 + 0)
    parm _T257
    parm _T10
    _T258 = *(_T257 + 0)
    _T259 = *(_T258 + 8)
    call _T259
    branch _L75
_L76:
    _T260 = *(_T9 + 12)
    *(_T9 + 12) = _T10
}

FUNCTION(_BJDeck.DealCard) {
memo '_T11:4'
_BJDeck.DealCard:
    _T262 = 0
    _T261 = _T262
    _T263 = *(_T11 + 8)
    _T264 = 8
    _T265 = 52
    _T266 = (_T264 * _T265)
    _T267 = (_T263 >= _T266)
    if (_T267 == 0) branch _L81
    _T268 = 11
    return _T268
_L81:
_L82:
    _T269 = 0
    _T270 = (_T261 == _T269)
    if (_T270 == 0) branch _L83
    _T272 = *(_T11 + 12)
    _T273 = 8
    parm _T272
    parm _T273
    _T274 = *(_T272 + 0)
    _T275 = *(_T274 + 16)
    _T276 =  call _T275
    _T271 = _T276
    _T277 = *(_T11 + 4)
    _T278 = *(_T277 - 4)
    _T279 = (_T271 < _T278)
    if (_T279 == 0) branch _L84
    _T280 = 0
    _T281 = (_T271 < _T280)
    if (_T281 == 0) branch _L85
_L84:
    _T282 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T282
    call _PrintString
    call _Halt
_L85:
    _T283 = 4
    _T284 = (_T271 * _T283)
    _T285 = (_T277 + _T284)
    _T286 = *(_T285 + 0)
    parm _T286
    _T287 = *(_T286 + 0)
    _T288 = *(_T287 + 16)
    _T289 =  call _T288
    _T261 = _T289
    branch _L82
_L83:
    _T290 = 10
    _T291 = (_T261 > _T290)
    if (_T291 == 0) branch _L86
    _T292 = 10
    _T261 = _T292
    branch _L87
_L86:
    _T293 = 1
    _T294 = (_T261 == _T293)
    if (_T294 == 0) branch _L88
    _T295 = 11
    _T261 = _T295
_L88:
_L87:
    _T296 = *(_T11 + 8)
    _T297 = *(_T11 + 8)
    _T298 = 1
    _T299 = (_T297 + _T298)
    *(_T11 + 8) = _T299
    return _T261
}

FUNCTION(_BJDeck.Shuffle) {
memo '_T12:4'
_BJDeck.Shuffle:
    _T301 = "Shuffling..."
    parm _T301
    call _PrintString
    _T302 = 0
    _T300 = _T302
    branch _L89
_L90:
    _T303 = 1
    _T304 = (_T300 + _T303)
    _T300 = _T304
_L89:
    _T305 = 8
    _T306 = (_T300 < _T305)
    if (_T306 == 0) branch _L91
    _T307 = *(_T12 + 4)
    _T308 = *(_T307 - 4)
    _T309 = (_T300 < _T308)
    if (_T309 == 0) branch _L92
    _T310 = 0
    _T311 = (_T300 < _T310)
    if (_T311 == 0) branch _L93
_L92:
    _T312 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T312
    call _PrintString
    call _Halt
_L93:
    _T313 = 4
    _T314 = (_T300 * _T313)
    _T315 = (_T307 + _T314)
    _T316 = *(_T315 + 0)
    parm _T316
    _T317 = *(_T316 + 0)
    _T318 = *(_T317 + 12)
    call _T318
    branch _L90
_L91:
    _T319 = *(_T12 + 8)
    _T320 = 0
    *(_T12 + 8) = _T320
    _T321 = "done.\n"
    parm _T321
    call _PrintString
}

FUNCTION(_BJDeck.NumCardsRemaining) {
memo '_T13:4'
_BJDeck.NumCardsRemaining:
    _T322 = 8
    _T323 = 52
    _T324 = (_T322 * _T323)
    _T325 = *(_T13 + 8)
    _T326 = (_T324 - _T325)
    return _T326
}

FUNCTION(_Player.Init) {
memo '_T14:4 _T15:8'
_Player.Init:
    _T327 = *(_T14 + 20)
    _T328 = 1000
    *(_T14 + 20) = _T328
    _T329 = "What is the name of player #"
    parm _T329
    call _PrintString
    parm _T15
    call _PrintInt
    _T330 = "? "
    parm _T330
    call _PrintString
    _T331 = *(_T14 + 24)
    _T332 =  call _ReadLine
    *(_T14 + 24) = _T332
}

FUNCTION(_Player.Hit) {
memo '_T16:4 _T17:8'
_Player.Hit:
    parm _T17
    _T334 = *(_T17 + 0)
    _T335 = *(_T334 + 12)
    _T336 =  call _T335
    _T333 = _T336
    _T337 = *(_T16 + 24)
    parm _T337
    call _PrintString
    _T338 = " was dealt a "
    parm _T338
    call _PrintString
    parm _T333
    call _PrintInt
    _T339 = ".\n"
    parm _T339
    call _PrintString
    _T340 = *(_T16 + 4)
    _T341 = *(_T16 + 4)
    _T342 = (_T341 + _T333)
    *(_T16 + 4) = _T342
    _T343 = *(_T16 + 12)
    _T344 = *(_T16 + 12)
    _T345 = 1
    _T346 = (_T344 + _T345)
    *(_T16 + 12) = _T346
    _T347 = 11
    _T348 = (_T333 == _T347)
    if (_T348 == 0) branch _L94
    _T349 = *(_T16 + 8)
    _T350 = *(_T16 + 8)
    _T351 = 1
    _T352 = (_T350 + _T351)
    *(_T16 + 8) = _T352
_L94:
_L95:
    _T353 = *(_T16 + 4)
    _T354 = 21
    _T355 = (_T353 > _T354)
    _T356 = *(_T16 + 8)
    _T357 = 0
    _T358 = (_T356 > _T357)
    _T359 = (_T355 && _T358)
    if (_T359 == 0) branch _L96
    _T360 = *(_T16 + 4)
    _T361 = *(_T16 + 4)
    _T362 = 10
    _T363 = (_T361 - _T362)
    *(_T16 + 4) = _T363
    _T364 = *(_T16 + 8)
    _T365 = *(_T16 + 8)
    _T366 = 1
    _T367 = (_T365 - _T366)
    *(_T16 + 8) = _T367
    branch _L95
_L96:
}

FUNCTION(_Player.DoubleDown) {
memo '_T18:4 _T19:8'
_Player.DoubleDown:
    _T369 = *(_T18 + 4)
    _T370 = 10
    _T371 = (_T369 != _T370)
    _T372 = *(_T18 + 4)
    _T373 = 11
    _T374 = (_T372 != _T373)
    _T375 = (_T371 && _T374)
    if (_T375 == 0) branch _L97
    _T376 = 0
    return _T376
_L97:
    _T377 = "Would you like to double down?"
    parm _T18
    parm _T377
    _T378 = *(_T18 + 0)
    _T379 = *(_T378 + 44)
    _T380 =  call _T379
    if (_T380 == 0) branch _L98
    _T381 = *(_T18 + 16)
    _T382 = *(_T18 + 16)
    _T383 = 2
    _T384 = (_T382 * _T383)
    *(_T18 + 16) = _T384
    parm _T18
    parm _T19
    _T385 = *(_T18 + 0)
    _T386 = *(_T385 + 12)
    call _T386
    _T387 = *(_T18 + 24)
    parm _T387
    call _PrintString
    _T388 = ", your total is "
    parm _T388
    call _PrintString
    _T389 = *(_T18 + 4)
    parm _T389
    call _PrintInt
    _T390 = ".\n"
    parm _T390
    call _PrintString
    _T391 = 1
    return _T391
    branch _L99
_L98:
    _T392 = 0
    return _T392
_L99:
}

FUNCTION(_Player.TakeTurn) {
memo '_T20:4 _T21:8'
_Player.TakeTurn:
    _T394 = "\n"
    parm _T394
    call _PrintString
    _T395 = *(_T20 + 24)
    parm _T395
    call _PrintString
    _T396 = "'s turn.\n"
    parm _T396
    call _PrintString
    _T397 = *(_T20 + 4)
    _T398 = 0
    *(_T20 + 4) = _T398
    _T399 = *(_T20 + 8)
    _T400 = 0
    *(_T20 + 8) = _T400
    _T401 = *(_T20 + 12)
    _T402 = 0
    *(_T20 + 12) = _T402
    parm _T20
    parm _T21
    _T403 = *(_T20 + 0)
    _T404 = *(_T403 + 12)
    call _T404
    parm _T20
    parm _T21
    _T405 = *(_T20 + 0)
    _T406 = *(_T405 + 12)
    call _T406
    parm _T20
    parm _T21
    _T407 = *(_T20 + 0)
    _T408 = *(_T407 + 16)
    _T409 =  call _T408
    _T410 = ! _T409
    if (_T410 == 0) branch _L100
    _T411 = 1
    _T393 = _T411
_L101:
    _T412 = *(_T20 + 4)
    _T413 = 21
    _T414 = (_T412 <= _T413)
    _T415 = (_T414 && _T393)
    if (_T415 == 0) branch _L102
    _T416 = *(_T20 + 24)
    parm _T416
    call _PrintString
    _T417 = ", your total is "
    parm _T417
    call _PrintString
    _T418 = *(_T20 + 4)
    parm _T418
    call _PrintInt
    _T419 = ".\n"
    parm _T419
    call _PrintString
    _T420 = "Would you like a hit?"
    parm _T20
    parm _T420
    _T421 = *(_T20 + 0)
    _T422 = *(_T421 + 44)
    _T423 =  call _T422
    _T393 = _T423
    if (_T393 == 0) branch _L103
    parm _T20
    parm _T21
    _T424 = *(_T20 + 0)
    _T425 = *(_T424 + 12)
    call _T425
_L103:
    branch _L101
_L102:
_L100:
    _T426 = *(_T20 + 4)
    _T427 = 21
    _T428 = (_T426 > _T427)
    if (_T428 == 0) branch _L104
    _T429 = *(_T20 + 24)
    parm _T429
    call _PrintString
    _T430 = " busts with the big "
    parm _T430
    call _PrintString
    _T431 = *(_T20 + 4)
    parm _T431
    call _PrintInt
    _T432 = "!\n"
    parm _T432
    call _PrintString
    branch _L105
_L104:
    _T433 = *(_T20 + 24)
    parm _T433
    call _PrintString
    _T434 = " stays at "
    parm _T434
    call _PrintString
    _T435 = *(_T20 + 4)
    parm _T435
    call _PrintInt
    _T436 = ".\n"
    parm _T436
    call _PrintString
_L105:
}

FUNCTION(_Player.HasMoney) {
memo '_T22:4'
_Player.HasMoney:
    _T437 = *(_T22 + 20)
    _T438 = 0
    _T439 = (_T437 > _T438)
    return _T439
}

FUNCTION(_Player.PrintMoney) {
memo '_T23:4'
_Player.PrintMoney:
    _T440 = *(_T23 + 24)
    parm _T440
    call _PrintString
    _T441 = ", you have $"
    parm _T441
    call _PrintString
    _T442 = *(_T23 + 20)
    parm _T442
    call _PrintInt
    _T443 = ".\n"
    parm _T443
    call _PrintString
}

FUNCTION(_Player.PlaceBet) {
memo '_T24:4'
_Player.PlaceBet:
    _T444 = *(_T24 + 16)
    _T445 = 0
    *(_T24 + 16) = _T445
    parm _T24
    _T446 = *(_T24 + 0)
    _T447 = *(_T446 + 28)
    call _T447
_L106:
    _T448 = *(_T24 + 16)
    _T449 = 0
    _T450 = (_T448 <= _T449)
    _T451 = *(_T24 + 16)
    _T452 = *(_T24 + 20)
    _T453 = (_T451 > _T452)
    _T454 = (_T450 || _T453)
    if (_T454 == 0) branch _L107
    _T455 = "How much would you like to bet? "
    parm _T455
    call _PrintString
    _T456 = *(_T24 + 16)
    _T457 =  call _ReadInteger
    *(_T24 + 16) = _T457
    branch _L106
_L107:
}

FUNCTION(_Player.GetTotal) {
memo '_T25:4'
_Player.GetTotal:
    _T458 = *(_T25 + 4)
    return _T458
}

FUNCTION(_Player.Resolve) {
memo '_T26:4 _T27:8'
_Player.Resolve:
    _T461 = 0
    _T459 = _T461
    _T462 = 0
    _T460 = _T462
    _T463 = *(_T26 + 4)
    _T464 = 21
    _T465 = (_T463 == _T464)
    _T466 = *(_T26 + 12)
    _T467 = 2
    _T468 = (_T466 == _T467)
    _T469 = (_T465 && _T468)
    if (_T469 == 0) branch _L108
    _T470 = 2
    _T459 = _T470
    branch _L109
_L108:
    _T471 = *(_T26 + 4)
    _T472 = 21
    _T473 = (_T471 > _T472)
    if (_T473 == 0) branch _L110
    _T474 = 1
    _T460 = _T474
    branch _L111
_L110:
    _T475 = 21
    _T476 = (_T27 > _T475)
    if (_T476 == 0) branch _L112
    _T477 = 1
    _T459 = _T477
    branch _L113
_L112:
    _T478 = *(_T26 + 4)
    _T479 = (_T478 > _T27)
    if (_T479 == 0) branch _L114
    _T480 = 1
    _T459 = _T480
    branch _L115
_L114:
    _T481 = *(_T26 + 4)
    _T482 = (_T27 > _T481)
    if (_T482 == 0) branch _L116
    _T483 = 1
    _T460 = _T483
_L116:
_L115:
_L113:
_L111:
_L109:
    _T484 = 1
    _T485 = (_T459 >= _T484)
    if (_T485 == 0) branch _L117
    _T486 = *(_T26 + 24)
    parm _T486
    call _PrintString
    _T487 = ", you won $"
    parm _T487
    call _PrintString
    _T488 = *(_T26 + 16)
    parm _T488
    call _PrintInt
    _T489 = ".\n"
    parm _T489
    call _PrintString
    branch _L118
_L117:
    _T490 = 1
    _T491 = (_T460 >= _T490)
    if (_T491 == 0) branch _L119
    _T492 = *(_T26 + 24)
    parm _T492
    call _PrintString
    _T493 = ", you lost $"
    parm _T493
    call _PrintString
    _T494 = *(_T26 + 16)
    parm _T494
    call _PrintInt
    _T495 = ".\n"
    parm _T495
    call _PrintString
    branch _L120
_L119:
    _T496 = *(_T26 + 24)
    parm _T496
    call _PrintString
    _T497 = ", you push!\n"
    parm _T497
    call _PrintString
_L120:
_L118:
    _T498 = *(_T26 + 16)
    _T499 = (_T459 * _T498)
    _T459 = _T499
    _T500 = *(_T26 + 16)
    _T501 = (_T460 * _T500)
    _T460 = _T501
    _T502 = *(_T26 + 20)
    _T503 = *(_T26 + 20)
    _T504 = (_T503 + _T459)
    _T505 = (_T504 - _T460)
    *(_T26 + 20) = _T505
}

FUNCTION(_Player.GetYesOrNo) {
memo '_T28:4 _T29:8'
_Player.GetYesOrNo:
    parm _T29
    call _PrintString
    _T506 = " (0=No/1=Yes) "
    parm _T506
    call _PrintString
    _T507 =  call _ReadInteger
    _T508 = 0
    _T509 = (_T507 != _T508)
    return _T509
}

FUNCTION(_Dealer.Init) {
memo '_T30:4 _T31:8'
_Dealer.Init:
    _T511 = *(_T30 + 4)
    _T512 = 0
    *(_T30 + 4) = _T512
    _T513 = *(_T30 + 8)
    _T514 = 0
    *(_T30 + 8) = _T514
    _T515 = *(_T30 + 12)
    _T516 = 0
    *(_T30 + 12) = _T516
    _T517 = "Dealer"
    _T510 = _T517
    _T518 = *(_T30 + 24)
    *(_T30 + 24) = _T510
}

FUNCTION(_Dealer.TakeTurn) {
memo '_T32:4 _T33:8'
_Dealer.TakeTurn:
    _T519 = "\n"
    parm _T519
    call _PrintString
    _T520 = *(_T32 + 24)
    parm _T520
    call _PrintString
    _T521 = "'s turn.\n"
    parm _T521
    call _PrintString
_L121:
    _T522 = *(_T32 + 4)
    _T523 = 16
    _T524 = (_T522 <= _T523)
    if (_T524 == 0) branch _L122
    parm _T32
    parm _T33
    _T525 = *(_T32 + 0)
    _T526 = *(_T525 + 12)
    call _T526
    branch _L121
_L122:
    _T527 = *(_T32 + 4)
    _T528 = 21
    _T529 = (_T527 > _T528)
    if (_T529 == 0) branch _L123
    _T530 = *(_T32 + 24)
    parm _T530
    call _PrintString
    _T531 = " busts with the big "
    parm _T531
    call _PrintString
    _T532 = *(_T32 + 4)
    parm _T532
    call _PrintInt
    _T533 = "!\n"
    parm _T533
    call _PrintString
    branch _L124
_L123:
    _T534 = *(_T32 + 24)
    parm _T534
    call _PrintString
    _T535 = " stays at "
    parm _T535
    call _PrintString
    _T536 = *(_T32 + 4)
    parm _T536
    call _PrintInt
    _T537 = ".\n"
    parm _T537
    call _PrintString
_L124:
}

FUNCTION(_House.SetupGame) {
memo '_T34:4'
_House.SetupGame:
    _T538 = "\nWelcome to CS143 BlackJack!\n"
    parm _T538
    call _PrintString
    _T539 = "---------------------------\n"
    parm _T539
    call _PrintString
    _T541 =  call _rndModule_New
    _T540 = _T541
    _T542 = "Please enter a random number seed: "
    parm _T542
    call _PrintString
    _T543 =  call _ReadInteger
    parm _T540
    parm _T543
    _T544 = *(_T540 + 0)
    _T545 = *(_T544 + 8)
    call _T545
    _T546 = *(_T34 + 12)
    _T547 =  call _BJDeck_New
    *(_T34 + 12) = _T547
    _T548 = *(_T34 + 8)
    _T549 =  call _Dealer_New
    *(_T34 + 8) = _T549
    _T550 = *(_T34 + 12)
    parm _T550
    parm _T540
    _T551 = *(_T550 + 0)
    _T552 = *(_T551 + 8)
    call _T552
    _T553 = *(_T34 + 12)
    parm _T553
    _T554 = *(_T553 + 0)
    _T555 = *(_T554 + 16)
    call _T555
}

FUNCTION(_House.SetupPlayers) {
memo '_T35:4'
_House.SetupPlayers:
    _T558 = "How many players do we have today? "
    parm _T558
    call _PrintString
    _T559 =  call _ReadInteger
    _T557 = _T559
    _T560 = *(_T35 + 4)
    _T561 = 0
    _T562 = (_T557 < _T561)
    if (_T562 == 0) branch _L125
    _T563 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T563
    call _PrintString
    call _Halt
_L125:
    _T564 = 4
    _T565 = (_T564 * _T557)
    _T566 = (_T564 + _T565)
    parm _T566
    _T567 =  call _Alloc
    *(_T567 + 0) = _T557
    _T568 = 0
    _T567 = (_T567 + _T566)
_L126:
    _T566 = (_T566 - _T564)
    if (_T566 == 0) branch _L127
    _T567 = (_T567 - _T564)
    *(_T567 + 0) = _T568
    branch _L126
_L127:
    *(_T35 + 4) = _T567
    _T569 = 0
    _T556 = _T569
    branch _L128
_L129:
    _T570 = 1
    _T571 = (_T556 + _T570)
    _T556 = _T571
_L128:
    _T572 = *(_T35 + 4)
    _T573 = *(_T572 - 4)
    _T574 = (_T556 < _T573)
    if (_T574 == 0) branch _L130
    _T575 = *(_T35 + 4)
    _T576 = *(_T575 - 4)
    _T577 = (_T556 < _T576)
    if (_T577 == 0) branch _L131
    _T578 = 0
    _T579 = (_T556 < _T578)
    if (_T579 == 0) branch _L132
_L131:
    _T580 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T580
    call _PrintString
    call _Halt
_L132:
    _T581 = 4
    _T582 = (_T556 * _T581)
    _T583 = (_T575 + _T582)
    _T584 = *(_T583 + 0)
    _T585 =  call _Player_New
    _T586 = 4
    _T587 = (_T556 * _T586)
    _T588 = (_T575 + _T587)
    *(_T588 + 0) = _T585
    _T589 = *(_T35 + 4)
    _T590 = *(_T589 - 4)
    _T591 = (_T556 < _T590)
    if (_T591 == 0) branch _L133
    _T592 = 0
    _T593 = (_T556 < _T592)
    if (_T593 == 0) branch _L134
_L133:
    _T594 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T594
    call _PrintString
    call _Halt
_L134:
    _T595 = 4
    _T596 = (_T556 * _T595)
    _T597 = (_T589 + _T596)
    _T598 = *(_T597 + 0)
    _T599 = 1
    _T600 = (_T556 + _T599)
    parm _T598
    parm _T600
    _T601 = *(_T598 + 0)
    _T602 = *(_T601 + 8)
    call _T602
    branch _L129
_L130:
}

FUNCTION(_House.TakeAllBets) {
memo '_T36:4'
_House.TakeAllBets:
    _T604 = "\nFirst, let's take bets.\n"
    parm _T604
    call _PrintString
    _T605 = 0
    _T603 = _T605
    branch _L135
_L136:
    _T606 = 1
    _T607 = (_T603 + _T606)
    _T603 = _T607
_L135:
    _T608 = *(_T36 + 4)
    _T609 = *(_T608 - 4)
    _T610 = (_T603 < _T609)
    if (_T610 == 0) branch _L137
    _T611 = *(_T36 + 4)
    _T612 = *(_T611 - 4)
    _T613 = (_T603 < _T612)
    if (_T613 == 0) branch _L138
    _T614 = 0
    _T615 = (_T603 < _T614)
    if (_T615 == 0) branch _L139
_L138:
    _T616 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T616
    call _PrintString
    call _Halt
_L139:
    _T617 = 4
    _T618 = (_T603 * _T617)
    _T619 = (_T611 + _T618)
    _T620 = *(_T619 + 0)
    parm _T620
    _T621 = *(_T620 + 0)
    _T622 = *(_T621 + 24)
    _T623 =  call _T622
    if (_T623 == 0) branch _L140
    _T624 = *(_T36 + 4)
    _T625 = *(_T624 - 4)
    _T626 = (_T603 < _T625)
    if (_T626 == 0) branch _L141
    _T627 = 0
    _T628 = (_T603 < _T627)
    if (_T628 == 0) branch _L142
_L141:
    _T629 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T629
    call _PrintString
    call _Halt
_L142:
    _T630 = 4
    _T631 = (_T603 * _T630)
    _T632 = (_T624 + _T631)
    _T633 = *(_T632 + 0)
    parm _T633
    _T634 = *(_T633 + 0)
    _T635 = *(_T634 + 32)
    call _T635
_L140:
    branch _L136
_L137:
}

FUNCTION(_House.TakeAllTurns) {
memo '_T37:4'
_House.TakeAllTurns:
    _T637 = 0
    _T636 = _T637
    branch _L143
_L144:
    _T638 = 1
    _T639 = (_T636 + _T638)
    _T636 = _T639
_L143:
    _T640 = *(_T37 + 4)
    _T641 = *(_T640 - 4)
    _T642 = (_T636 < _T641)
    if (_T642 == 0) branch _L145
    _T643 = *(_T37 + 4)
    _T644 = *(_T643 - 4)
    _T645 = (_T636 < _T644)
    if (_T645 == 0) branch _L146
    _T646 = 0
    _T647 = (_T636 < _T646)
    if (_T647 == 0) branch _L147
_L146:
    _T648 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T648
    call _PrintString
    call _Halt
_L147:
    _T649 = 4
    _T650 = (_T636 * _T649)
    _T651 = (_T643 + _T650)
    _T652 = *(_T651 + 0)
    parm _T652
    _T653 = *(_T652 + 0)
    _T654 = *(_T653 + 24)
    _T655 =  call _T654
    if (_T655 == 0) branch _L148
    _T656 = *(_T37 + 4)
    _T657 = *(_T656 - 4)
    _T658 = (_T636 < _T657)
    if (_T658 == 0) branch _L149
    _T659 = 0
    _T660 = (_T636 < _T659)
    if (_T660 == 0) branch _L150
_L149:
    _T661 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T661
    call _PrintString
    call _Halt
_L150:
    _T662 = 4
    _T663 = (_T636 * _T662)
    _T664 = (_T656 + _T663)
    _T665 = *(_T664 + 0)
    _T666 = *(_T37 + 12)
    parm _T665
    parm _T666
    _T667 = *(_T665 + 0)
    _T668 = *(_T667 + 20)
    call _T668
_L148:
    branch _L144
_L145:
}

FUNCTION(_House.ResolveAllPlayers) {
memo '_T38:4'
_House.ResolveAllPlayers:
    _T670 = "\nTime to resolve bets.\n"
    parm _T670
    call _PrintString
    _T671 = 0
    _T669 = _T671
    branch _L151
_L152:
    _T672 = 1
    _T673 = (_T669 + _T672)
    _T669 = _T673
_L151:
    _T674 = *(_T38 + 4)
    _T675 = *(_T674 - 4)
    _T676 = (_T669 < _T675)
    if (_T676 == 0) branch _L153
    _T677 = *(_T38 + 4)
    _T678 = *(_T677 - 4)
    _T679 = (_T669 < _T678)
    if (_T679 == 0) branch _L154
    _T680 = 0
    _T681 = (_T669 < _T680)
    if (_T681 == 0) branch _L155
_L154:
    _T682 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T682
    call _PrintString
    call _Halt
_L155:
    _T683 = 4
    _T684 = (_T669 * _T683)
    _T685 = (_T677 + _T684)
    _T686 = *(_T685 + 0)
    parm _T686
    _T687 = *(_T686 + 0)
    _T688 = *(_T687 + 24)
    _T689 =  call _T688
    if (_T689 == 0) branch _L156
    _T690 = *(_T38 + 4)
    _T691 = *(_T690 - 4)
    _T692 = (_T669 < _T691)
    if (_T692 == 0) branch _L157
    _T693 = 0
    _T694 = (_T669 < _T693)
    if (_T694 == 0) branch _L158
_L157:
    _T695 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T695
    call _PrintString
    call _Halt
_L158:
    _T696 = 4
    _T697 = (_T669 * _T696)
    _T698 = (_T690 + _T697)
    _T699 = *(_T698 + 0)
    _T700 = *(_T38 + 8)
    parm _T700
    _T701 = *(_T700 + 0)
    _T702 = *(_T701 + 36)
    _T703 =  call _T702
    parm _T699
    parm _T703
    _T704 = *(_T699 + 0)
    _T705 = *(_T704 + 40)
    call _T705
_L156:
    branch _L152
_L153:
}

FUNCTION(_House.PrintAllMoney) {
memo '_T39:4'
_House.PrintAllMoney:
    _T707 = 0
    _T706 = _T707
    branch _L159
_L160:
    _T708 = 1
    _T709 = (_T706 + _T708)
    _T706 = _T709
_L159:
    _T710 = *(_T39 + 4)
    _T711 = *(_T710 - 4)
    _T712 = (_T706 < _T711)
    if (_T712 == 0) branch _L161
    _T713 = *(_T39 + 4)
    _T714 = *(_T713 - 4)
    _T715 = (_T706 < _T714)
    if (_T715 == 0) branch _L162
    _T716 = 0
    _T717 = (_T706 < _T716)
    if (_T717 == 0) branch _L163
_L162:
    _T718 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T718
    call _PrintString
    call _Halt
_L163:
    _T719 = 4
    _T720 = (_T706 * _T719)
    _T721 = (_T713 + _T720)
    _T722 = *(_T721 + 0)
    parm _T722
    _T723 = *(_T722 + 0)
    _T724 = *(_T723 + 28)
    call _T724
    branch _L160
_L161:
}

FUNCTION(_House.PlayOneGame) {
memo '_T40:4'
_House.PlayOneGame:
    _T725 = *(_T40 + 12)
    parm _T725
    _T726 = *(_T725 + 0)
    _T727 = *(_T726 + 20)
    _T728 =  call _T727
    _T729 = 26
    _T730 = (_T728 < _T729)
    if (_T730 == 0) branch _L164
    _T731 = *(_T40 + 12)
    parm _T731
    _T732 = *(_T731 + 0)
    _T733 = *(_T732 + 16)
    call _T733
_L164:
    parm _T40
    _T734 = *(_T40 + 0)
    _T735 = *(_T734 + 16)
    call _T735
    _T736 = "\nDealer starts. "
    parm _T736
    call _PrintString
    _T737 = *(_T40 + 8)
    _T738 = 0
    parm _T737
    parm _T738
    _T739 = *(_T737 + 0)
    _T740 = *(_T739 + 8)
    call _T740
    _T741 = *(_T40 + 8)
    _T742 = *(_T40 + 12)
    parm _T741
    parm _T742
    _T743 = *(_T741 + 0)
    _T744 = *(_T743 + 12)
    call _T744
    parm _T40
    _T745 = *(_T40 + 0)
    _T746 = *(_T745 + 20)
    call _T746
    _T747 = *(_T40 + 8)
    _T748 = *(_T40 + 12)
    parm _T747
    parm _T748
    _T749 = *(_T747 + 0)
    _T750 = *(_T749 + 20)
    call _T750
    parm _T40
    _T751 = *(_T40 + 0)
    _T752 = *(_T751 + 24)
    call _T752
}

FUNCTION(main) {
memo ''
main:
    _T754 = 1
    _T753 = _T754
    _T756 =  call _House_New
    _T755 = _T756
    parm _T755
    _T757 = *(_T755 + 0)
    _T758 = *(_T757 + 8)
    call _T758
    parm _T755
    _T759 = *(_T755 + 0)
    _T760 = *(_T759 + 12)
    call _T760
_L165:
    if (_T753 == 0) branch _L166
    parm _T755
    _T761 = *(_T755 + 0)
    _T762 = *(_T761 + 32)
    call _T762
    _T763 = "\nDo you want to play another hand?"
    parm _T763
    _T764 =  call _Main.GetYesOrNo
    _T753 = _T764
    branch _L165
_L166:
    parm _T755
    _T765 = *(_T755 + 0)
    _T766 = *(_T765 + 28)
    call _T766
    _T767 = "Thank you for playing...come again soon.\n"
    parm _T767
    call _PrintString
    _T768 = "\nCS143 BlackJack Copyright (c) 1999 by Peter Mork.\n"
    parm _T768
    call _PrintString
    _T769 = "(2001 mods by jdz)\n"
    parm _T769
    call _PrintString
}

FUNCTION(_Main.GetYesOrNo) {
memo '_T41:4'
_Main.GetYesOrNo:
    parm _T41
    call _PrintString
    _T770 = " (0=No/1=Yes) "
    parm _T770
    call _PrintString
    _T771 =  call _ReadInteger
    _T772 = 0
    _T773 = (_T771 != _T772)
    return _T773
}

