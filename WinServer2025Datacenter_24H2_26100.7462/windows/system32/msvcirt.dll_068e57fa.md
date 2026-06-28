# Binary Specification: msvcirt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcirt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `068e57fa60830c6cc9f1054f459d1a96b2e0fb4a59cc0c4e9bb53e40228f00e4`
* **Total Exported Functions:** 411

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 410 | `_mtlock` | `0x1290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_mtunlock` | `0x12C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0filebuf@@QEAA@AEBV0@@Z` | `0x12D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0fstream@@QEAA@AEBV0@@Z` | `0x1380` | 134 | UnwindData |  |
| 15 | `??0ifstream@@QEAA@AEBV0@@Z` | `0x1410` | 123 | UnwindData |  |
| 23 | `??0iostream@@IEAA@AEBV0@@Z` | `0x14A0` | 141 | UnwindData |  |
| 24 | `??0iostream@@IEAA@XZ` | `0x1540` | 119 | UnwindData |  |
| 25 | `??0iostream@@QEAA@PEAVstreambuf@@@Z` | `0x15C0` | 140 | UnwindData |  |
| 29 | `??0istream_withassign@@QEAA@AEBV0@@Z` | `0x1660` | 123 | UnwindData |  |
| 32 | `??0istrstream@@QEAA@AEBV0@@Z` | `0x16F0` | 123 | UnwindData |  |
| 38 | `??0ofstream@@QEAA@AEBV0@@Z` | `0x1780` | 123 | UnwindData |  |
| 46 | `??0ostream_withassign@@QEAA@AEBV0@@Z` | `0x1810` | 123 | UnwindData |  |
| 49 | `??0ostrstream@@QEAA@AEBV0@@Z` | `0x18A0` | 123 | UnwindData |  |
| 52 | `??0stdiobuf@@QEAA@AEBV0@@Z` | `0x1930` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0stdiostream@@QEAA@AEBV0@@Z` | `0x19E0` | 134 | UnwindData |  |
| 58 | `??0streambuf@@QEAA@AEBV0@@Z` | `0x1A70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??0strstream@@QEAA@AEBV0@@Z` | `0x1B00` | 134 | UnwindData |  |
| 62 | `??0strstreambuf@@QEAA@AEBV0@@Z` | `0x1B90` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??1iostream@@UEAA@XZ` | `0x1C80` | 48 | UnwindData |  |
| 2 | `??0Iostream_init@@QEAA@XZ` | `0x1CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??4Iostream_init@@QEAAAEAV0@AEBV0@@Z` | `0x1CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??4filebuf@@QEAAAEAV0@AEBV0@@Z` | `0x1CD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??4fstream@@QEAAAEAV0@AEAV0@@Z` | `0x1D70` | 59 | UnwindData |  |
| 94 | `??4iostream@@IEAAAEAV0@AEAV0@@Z` | `0x1D70` | 59 | UnwindData |  |
| 112 | `??4stdiostream@@QEAAAEAV0@AEAV0@@Z` | `0x1D70` | 59 | UnwindData |  |
| 114 | `??4strstream@@QEAAAEAV0@AEAV0@@Z` | `0x1D70` | 59 | UnwindData |  |
| 92 | `??4ifstream@@QEAAAEAV0@AEBV0@@Z` | `0x1DC0` | 38 | UnwindData |  |
| 98 | `??4istream_withassign@@QEAAAEAV0@AEBV0@@Z` | `0x1DC0` | 38 | UnwindData |  |
| 101 | `??4istrstream@@QEAAAEAV0@AEBV0@@Z` | `0x1DC0` | 38 | UnwindData |  |
| 95 | `??4iostream@@IEAAAEAV0@PEAVstreambuf@@@Z` | `0x1DF0` | 47 | UnwindData |  |
| 96 | `??4istream@@IEAAAEAV0@AEBV0@@Z` | `0x1E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??4istream_withassign@@QEAAAEAVistream@@AEBV1@@Z` | `0x1E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `??4istream_withassign@@QEAAAEAVistream@@PEAVstreambuf@@@Z` | `0x1E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??4ofstream@@QEAAAEAV0@AEBV0@@Z` | `0x1E60` | 38 | UnwindData |  |
| 107 | `??4ostream_withassign@@QEAAAEAV0@AEBV0@@Z` | `0x1E60` | 38 | UnwindData |  |
| 110 | `??4ostrstream@@QEAAAEAV0@AEBV0@@Z` | `0x1E60` | 38 | UnwindData |  |
| 105 | `??4ostream@@IEAAAEAV0@AEBV0@@Z` | `0x1E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??4ostream_withassign@@QEAAAEAVostream@@AEBV1@@Z` | `0x1E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??4ostream_withassign@@QEAAAEAVostream@@PEAVstreambuf@@@Z` | `0x1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??4stdiobuf@@QEAAAEAV0@AEBV0@@Z` | `0x1EC0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??4streambuf@@QEAAAEAV0@AEBV0@@Z` | `0x1F50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??4strstreambuf@@QEAAAEAV0@AEBV0@@Z` | `0x1FE0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??5istream@@QEAAAEAV0@AEAC@Z` | `0x20B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??5istream@@QEAAAEAV0@AEAE@Z` | `0x20B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??5istream@@QEAAAEAV0@P6AAEAV0@AEAV0@@Z@Z` | `0x20C0` | 26 | UnwindData |  |
| 146 | `??6ostream@@QEAAAEAV0@P6AAEAV0@AEAV0@@Z@Z` | `0x20C0` | 26 | UnwindData |  |
| 129 | `??5istream@@QEAAAEAV0@P6AAEAVios@@AEAV1@@Z@Z` | `0x20E0` | 36 | UnwindData |  |
| 147 | `??6ostream@@QEAAAEAV0@P6AAEAVios@@AEAV1@@Z@Z` | `0x20E0` | 36 | UnwindData |  |
| 130 | `??5istream@@QEAAAEAV0@PEAC@Z` | `0x2110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??5istream@@QEAAAEAV0@PEAE@Z` | `0x2110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??6ostream@@QEAAAEAV0@C@Z` | `0x2120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??6ostream@@QEAAAEAV0@D@Z` | `0x2120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??6ostream@@QEAAAEAV0@M@Z` | `0x2130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??6ostream@@QEAAAEAV0@PEBC@Z` | `0x2150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `??6ostream@@QEAAAEAV0@PEBE@Z` | `0x2150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `??7ios@@QEBAHXZ` | `0x2160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?fail@ios@@QEBAHXZ` | `0x2160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??Bios@@QEBAPEAXXZ` | `0x2170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `??_Dfstream@@QEAAXXZ` | `0x2190` | 31 | UnwindData |  |
| 191 | `??_Difstream@@QEAAXXZ` | `0x21C0` | 31 | UnwindData |  |
| 192 | `??_Diostream@@QEAAXXZ` | `0x21F0` | 31 | UnwindData |  |
| 193 | `??_Distream@@QEAAXXZ` | `0x2220` | 31 | UnwindData |  |
| 194 | `??_Distream_withassign@@QEAAXXZ` | `0x2250` | 31 | UnwindData |  |
| 195 | `??_Distrstream@@QEAAXXZ` | `0x2280` | 31 | UnwindData |  |
| 196 | `??_Dofstream@@QEAAXXZ` | `0x22B0` | 31 | UnwindData |  |
| 197 | `??_Dostream@@QEAAXXZ` | `0x22E0` | 31 | UnwindData |  |
| 198 | `??_Dostream_withassign@@QEAAXXZ` | `0x2310` | 31 | UnwindData |  |
| 199 | `??_Dostrstream@@QEAAXXZ` | `0x2340` | 31 | UnwindData |  |
| 200 | `??_Dstdiostream@@QEAAXXZ` | `0x2370` | 31 | UnwindData |  |
| 201 | `??_Dstrstream@@QEAAXXZ` | `0x23A0` | 31 | UnwindData |  |
| 205 | `?assign_default@ios@@IEAAXXZ` | `0x2B70` | 63 | UnwindData |  |
| 210 | `?bad@ios@@QEBAHXZ` | `0x2BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?base@streambuf@@IEBAPEADXZ` | `0x2BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?blen@streambuf@@IEBAHXZ` | `0x2BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `?clear@ios@@QEAAXH@Z` | `0x2C00` | 69 | UnwindData |  |
| 224 | `?clrlock@ios@@QEAAXXZ` | `0x2C50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?clrlock@streambuf@@QEAAXXZ` | `0x2C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?dec@@YAAEAVios@@AEAV1@@Z` | `0x2CA0` | 35 | UnwindData |  |
| 229 | `?delbuf@ios@@QEAAXH@Z` | `0x2CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?delbuf@ios@@QEBAHXZ` | `0x2CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?eback@streambuf@@IEBAPEADXZ` | `0x2CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?ebuf@streambuf@@IEBAPEADXZ` | `0x2D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?egptr@streambuf@@IEBAPEADXZ` | `0x2D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?endl@@YAAEAVostream@@AEAV1@@Z` | `0x2D20` | 33 | UnwindData |  |
| 238 | `?ends@@YAAEAVostream@@AEAV1@@Z` | `0x2D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `?eof@ios@@QEBAHXZ` | `0x2D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `?epptr@streambuf@@IEBAPEADXZ` | `0x2D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?fd@filebuf@@QEBAHXZ` | `0x2D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?fd@fstream@@QEBAHXZ` | `0x2DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?fd@ifstream@@QEBAHXZ` | `0x2DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?fd@ofstream@@QEBAHXZ` | `0x2DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?fill@ios@@QEAADD@Z` | `0x2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `?fill@ios@@QEBADXZ` | `0x2DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `?flags@ios@@QEAAJJ@Z` | `0x2DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?flags@ios@@QEBAJXZ` | `0x2E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?flush@@YAAEAVostream@@AEAV1@@Z` | `0x2E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?gbump@streambuf@@IEAAXH@Z` | `0x2E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?gcount@istream@@QEBAHXZ` | `0x2E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `?unbuffered@streambuf@@IEBAHXZ` | `0x2E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?get@istream@@QEAAAEAV1@AEAC@Z` | `0x2E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `?get@istream@@QEAAAEAV1@AEAE@Z` | `0x2E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `?get@istream@@QEAAAEAV1@PEACHD@Z` | `0x2E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?get@istream@@QEAAAEAV1@PEADHD@Z` | `0x2E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?get@istream@@QEAAAEAV1@PEAEHD@Z` | `0x2E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?getline@istream@@QEAAAEAV1@PEACHD@Z` | `0x2E70` | 127 | UnwindData |  |
| 269 | `?getline@istream@@QEAAAEAV1@PEADHD@Z` | `0x2E70` | 127 | UnwindData |  |
| 270 | `?getline@istream@@QEAAAEAV1@PEAEHD@Z` | `0x2E70` | 127 | UnwindData |  |
| 271 | `?good@ios@@QEBAHXZ` | `0x2F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?gptr@streambuf@@IEBAPEADXZ` | `0x2F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?hex@@YAAEAVios@@AEAV1@@Z` | `0x2F20` | 35 | UnwindData |  |
| 274 | `?ignore@istream@@QEAAAEAV1@HH@Z` | `0x2F50` | 112 | UnwindData |  |
| 275 | `?in_avail@streambuf@@QEBAHXZ` | `0x2FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?is_open@filebuf@@QEBAHXZ` | `0x2FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `?is_open@fstream@@QEBAHXZ` | `0x3010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `?is_open@ifstream@@QEBAHXZ` | `0x3010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `?is_open@ofstream@@QEBAHXZ` | `0x3010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?isfx@istream@@QEAAXXZ` | `0x3030` | 67 | UnwindData |  |
| 283 | `?iword@ios@@QEBAAEAJH@Z` | `0x3080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `?pword@ios@@QEBAAEAPEAXH@Z` | `0x3080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?lock@ios@@QEAAXXZ` | `0x30A0` | 24 | UnwindData |  |
| 285 | `?lock@streambuf@@QEAAXXZ` | `0x30C0` | 24 | UnwindData |  |
| 286 | `?lockbuf@ios@@QEAAXXZ` | `0x30E0` | 28 | UnwindData |  |
| 287 | `?lockc@ios@@KAXXZ` | `0x3110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?lockptr@ios@@IEAAPEAU_CRT_CRITICAL_SECTION@@XZ` | `0x3130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?lockptr@streambuf@@IEAAPEAU_CRT_CRITICAL_SECTION@@XZ` | `0x3140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `?oct@@YAAEAVios@@AEAV1@@Z` | `0x3150` | 35 | UnwindData |  |
| 298 | `?out_waiting@streambuf@@QEBAHXZ` | `0x3180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?pbase@streambuf@@IEBAPEADXZ` | `0x31A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `?tie@ios@@QEBAPEAVostream@@XZ` | `0x31A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?pbump@streambuf@@IEAAXH@Z` | `0x31B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?pcount@ostrstream@@QEBAHXZ` | `0x31D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?pcount@strstream@@QEBAHXZ` | `0x31D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?pptr@streambuf@@IEBAPEADXZ` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?precision@ios@@QEAAHH@Z` | `0x3210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `?precision@ios@@QEBAHXZ` | `0x3220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?put@ostream@@QEAAAEAV1@C@Z` | `0x3230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `?put@ostream@@QEAAAEAV1@D@Z` | `0x3230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `?rdbuf@fstream@@QEBAPEAVfilebuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `?rdbuf@ifstream@@QEBAPEAVfilebuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `?rdbuf@istrstream@@QEBAPEAVstrstreambuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `?rdbuf@ofstream@@QEBAPEAVfilebuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?rdbuf@ostrstream@@QEBAPEAVstrstreambuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `?rdbuf@stdiostream@@QEBAPEAVstdiobuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `?rdbuf@strstream@@QEBAPEAVstrstreambuf@@XZ` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `?rdbuf@ios@@QEBAPEAVstreambuf@@XZ` | `0x3260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `?rdstate@ios@@QEBAHXZ` | `0x3270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `?read@istream@@QEAAAEAV1@PEACH@Z` | `0x3280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `?read@istream@@QEAAAEAV1@PEAEH@Z` | `0x3280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `?setf@ios@@QEAAJJ@Z` | `0x3290` | 88 | UnwindData |  |
| 347 | `?setf@ios@@QEAAJJJ@Z` | `0x32F0` | 110 | UnwindData |  |
| 348 | `?setg@streambuf@@IEAAXPEAD00@Z` | `0x3370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `?setlock@ios@@QEAAXXZ` | `0x3390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `?setlock@streambuf@@QEAAXXZ` | `0x33B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `?setmode@fstream@@QEAAHH@Z` | `0x33C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `?setmode@ifstream@@QEAAHH@Z` | `0x33C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `?setmode@ofstream@@QEAAHH@Z` | `0x33C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `?setp@streambuf@@IEAAXPEAD0@Z` | `0x33E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `?sgetn@streambuf@@QEAAHPEADH@Z` | `0x3400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `?sputbackc@streambuf@@QEAAHD@Z` | `0x3420` | 55 | UnwindData |  |
| 364 | `?sputc@streambuf@@QEAAHH@Z` | `0x3460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `?sputn@streambuf@@QEAAHPEBDH@Z` | `0x3490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `?stdiofile@stdiobuf@@QEAAPEAU_iobuf@@XZ` | `0x34B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `?str@istrstream@@QEAAPEADXZ` | `0x34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `?str@ostrstream@@QEAAPEADXZ` | `0x34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `?str@strstream@@QEAAPEADXZ` | `0x34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `?tie@ios@@QEAAPEAVostream@@PEAV2@@Z` | `0x34E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `?unbuffered@streambuf@@IEAAXH@Z` | `0x34F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `?unlock@ios@@QEAAXXZ` | `0x3500` | 24 | UnwindData |  |
| 390 | `?unlock@streambuf@@QEAAXXZ` | `0x3520` | 24 | UnwindData |  |
| 391 | `?unlockbuf@ios@@QEAAXXZ` | `0x3540` | 28 | UnwindData |  |
| 392 | `?unlockc@ios@@KAXXZ` | `0x3570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `?unsetf@ios@@QEAAJJ@Z` | `0x3590` | 88 | UnwindData |  |
| 395 | `?width@ios@@QEAAHH@Z` | `0x35F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `?width@ios@@QEBAHXZ` | `0x3600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `?write@ostream@@QEAAAEAV1@PEBCH@Z` | `0x3610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `?write@ostream@@QEAAAEAV1@PEBEH@Z` | `0x3610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `?ws@@YAAEAVistream@@AEAV1@@Z` | `0x3620` | 23 | UnwindData |  |
| 1 | `??0Iostream_init@@QEAA@AEAVios@@H@Z` | `0x3640` | 100 | UnwindData |  |
| 68 | `??1Iostream_init@@QEAA@XZ` | `0x36B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0filebuf@@QEAA@H@Z` | `0x36C0` | 57 | UnwindData |  |
| 8 | `??0filebuf@@QEAA@HPEADH@Z` | `0x3700` | 114 | UnwindData |  |
| 9 | `??0filebuf@@QEAA@XZ` | `0x3780` | 47 | UnwindData |  |
| 70 | `??1filebuf@@UEAA@XZ` | `0x37C0` | 80 | UnwindData |  |
| 220 | `?close@filebuf@@QEAAPEAV1@XZ` | `0x3820` | 142 | UnwindData |  |
| 299 | `?overflow@filebuf@@UEAAHH@Z` | `0x38C0` | 155 | UnwindData |  |
| 332 | `?seekoff@filebuf@@UEAAJJW4seek_dir@ios@@H@Z` | `0x3970` | 113 | UnwindData |  |
| 340 | `?setbuf@filebuf@@UEAAPEAVstreambuf@@PEADH@Z` | `0x39F0` | 140 | UnwindData |  |
| 373 | `?sync@filebuf@@UEAAHXZ` | `0x3A90` | 332 | UnwindData |  |
| 386 | `?underflow@filebuf@@UEAAHXZ` | `0x3BF0` | 183 | UnwindData |  |
| 206 | `?attach@filebuf@@QEAAPEAV1@H@Z` | `0x3CB0` | 144 | UnwindData |  |
| 291 | `?open@filebuf@@QEAAPEAV1@PEBDHH@Z` | `0x3D50` | 510 | UnwindData |  |
| 351 | `?setmode@filebuf@@QEAAHH@Z` | `0x3F60` | 145 | UnwindData |  |
| 11 | `??0fstream@@QEAA@H@Z` | `0x4000` | 182 | UnwindData |  |
| 12 | `??0fstream@@QEAA@HPEADH@Z` | `0x40C0` | 220 | UnwindData |  |
| 13 | `??0fstream@@QEAA@PEBDHH@Z` | `0x41B0` | 266 | UnwindData |  |
| 14 | `??0fstream@@QEAA@XZ` | `0x42C0` | 182 | UnwindData |  |
| 71 | `??1fstream@@UEAA@XZ` | `0x4380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `?attach@fstream@@QEAAXH@Z` | `0x43A0` | 174 | UnwindData |  |
| 221 | `?close@fstream@@QEAAXXZ` | `0x4460` | 256 | UnwindData |  |
| 292 | `?open@fstream@@QEAAXPEBDHH@Z` | `0x4570` | 183 | UnwindData |  |
| 341 | `?setbuf@fstream@@QEAAPEAVstreambuf@@PEADH@Z` | `0x4630` | 206 | UnwindData |  |
| 16 | `??0ifstream@@QEAA@H@Z` | `0x4710` | 156 | UnwindData |  |
| 17 | `??0ifstream@@QEAA@HPEADH@Z` | `0x47C0` | 194 | UnwindData |  |
| 18 | `??0ifstream@@QEAA@PEBDHH@Z` | `0x4890` | 235 | UnwindData |  |
| 19 | `??0ifstream@@QEAA@XZ` | `0x4990` | 156 | UnwindData |  |
| 72 | `??1ifstream@@UEAA@XZ` | `0x4A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?attach@ifstream@@QEAAXH@Z` | `0x4A60` | 120 | UnwindData |  |
| 209 | `?attach@ofstream@@QEAAXH@Z` | `0x4A60` | 120 | UnwindData |  |
| 222 | `?close@ifstream@@QEAAXXZ` | `0x4AE0` | 116 | UnwindData |  |
| 223 | `?close@ofstream@@QEAAXXZ` | `0x4AE0` | 116 | UnwindData |  |
| 293 | `?open@ifstream@@QEAAXPEBDHH@Z` | `0x4B60` | 133 | UnwindData |  |
| 342 | `?setbuf@ifstream@@QEAAPEAVstreambuf@@PEADH@Z` | `0x4BF0` | 152 | UnwindData |  |
| 343 | `?setbuf@ofstream@@QEAAPEAVstreambuf@@PEADH@Z` | `0x4BF0` | 152 | UnwindData |  |
| 20 | `??0ios@@IEAA@AEBV0@@Z` | `0x4C90` | 87 | UnwindData |  |
| 21 | `??0ios@@IEAA@XZ` | `0x4CF0` | 114 | UnwindData |  |
| 22 | `??0ios@@QEAA@PEAVstreambuf@@@Z` | `0x4D70` | 120 | UnwindData |  |
| 73 | `??1ios@@UEAA@XZ` | `0x4DF0` | 109 | UnwindData |  |
| 93 | `??4ios@@IEAAAEAV0@AEBV0@@Z` | `0x4E70` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `?bitalloc@ios@@SAJXZ` | `0x4F30` | 53 | UnwindData |  |
| 276 | `?init@ios@@IEAAXPEAVstreambuf@@@Z` | `0x4F70` | 82 | UnwindData |  |
| 406 | `?xalloc@ios@@SAHXZ` | `0x4FD0` | 62 | UnwindData |  |
| 117 | `??5istream@@QEAAAEAV0@AEAD@Z` | `0x5020` | 131 | UnwindData |  |
| 126 | `??5istream@@QEAAAEAV0@AEAN@Z` | `0x50B0` | 161 | UnwindData |  |
| 26 | `??0istream@@IEAA@AEBV0@@Z` | `0x5160` | 146 | UnwindData |  |
| 27 | `??0istream@@IEAA@XZ` | `0x5200` | 79 | UnwindData |  |
| 28 | `??0istream@@QEAA@PEAVstreambuf@@@Z` | `0x5260` | 137 | UnwindData |  |
| 30 | `??0istream_withassign@@QEAA@PEAVstreambuf@@@Z` | `0x52F0` | 113 | UnwindData |  |
| 31 | `??0istream_withassign@@QEAA@XZ` | `0x5370` | 96 | UnwindData |  |
| 75 | `??1istream@@UEAA@XZ` | `0x53E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??1istream_withassign@@UEAA@XZ` | `0x5400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??4istream@@IEAAAEAV0@PEAVstreambuf@@@Z` | `0x5430` | 200 | UnwindData |  |
| 131 | `??5istream@@QEAAAEAV0@PEAD@Z` | `0x5500` | 281 | UnwindData |  |
| 233 | `?eatwhite@istream@@QEAAXXZ` | `0x56C0` | 205 | UnwindData |  |
| 277 | `?ipfx@istream@@QEAAHH@Z` | `0x57A0` | 269 | UnwindData |  |
| 308 | `?peek@istream@@QEAAHXZ` | `0x58C0` | 116 | UnwindData |  |
| 315 | `?putback@istream@@QEAAAEAV1@D@Z` | `0x5940` | 224 | UnwindData |  |
| 374 | `?sync@istream@@QEAAHXZ` | `0x5A30` | 199 | UnwindData |  |
| 133 | `??5istream@@QEAAAEAV0@PEAVstreambuf@@@Z` | `0x5B00` | 178 | UnwindData |  |
| 261 | `?get@istream@@QEAAAEAV1@AEAVstreambuf@@D@Z` | `0x5BC0` | 241 | UnwindData |  |
| 330 | `?seekg@istream@@QEAAAEAV1@J@Z` | `0x5CC0` | 194 | UnwindData |  |
| 331 | `?seekg@istream@@QEAAAEAV1@JW4seek_dir@ios@@@Z` | `0x5D90` | 200 | UnwindData |  |
| 379 | `?tellg@istream@@QEAAJXZ` | `0x5E60` | 209 | UnwindData |  |
| 125 | `??5istream@@QEAAAEAV0@AEAM@Z` | `0x5F40` | 270 | UnwindData |  |
| 266 | `?getdouble@istream@@AEAAHPEADH@Z` | `0x6060` | 474 | UnwindData |  |
| 259 | `?get@istream@@QEAAAEAV1@AEAD@Z` | `0x6240` | 137 | UnwindData |  |
| 265 | `?get@istream@@QEAAHXZ` | `0x62D0` | 138 | UnwindData |  |
| 327 | `?read@istream@@QEAAAEAV1@PEADH@Z` | `0x6360` | 158 | UnwindData |  |
| 257 | `?get@istream@@IEAAAEAV1@PEADHH@Z` | `0x6410` | 308 | UnwindData |  |
| 267 | `?getint@istream@@AEAAHPEAD@Z` | `0x6550` | 519 | UnwindData |  |
| 121 | `??5istream@@QEAAAEAV0@AEAH@Z` | `0x6760` | 152 | UnwindData |  |
| 127 | `??5istream@@QEAAAEAV0@AEAO@Z` | `0x6800` | 161 | UnwindData |  |
| 123 | `??5istream@@QEAAAEAV0@AEAJ@Z` | `0x68B0` | 175 | UnwindData |  |
| 119 | `??5istream@@QEAAAEAV0@AEAF@Z` | `0x6970` | 188 | UnwindData |  |
| 122 | `??5istream@@QEAAAEAV0@AEAI@Z` | `0x6A40` | 196 | UnwindData |  |
| 124 | `??5istream@@QEAAAEAV0@AEAK@Z` | `0x6B10` | 180 | UnwindData |  |
| 120 | `??5istream@@QEAAAEAV0@AEAG@Z` | `0x6BD0` | 216 | UnwindData |  |
| 39 | `??0ofstream@@QEAA@H@Z` | `0x6CB0` | 156 | UnwindData |  |
| 40 | `??0ofstream@@QEAA@HPEADH@Z` | `0x6D60` | 194 | UnwindData |  |
| 41 | `??0ofstream@@QEAA@PEBDHH@Z` | `0x6E30` | 235 | UnwindData |  |
| 42 | `??0ofstream@@QEAA@XZ` | `0x6F30` | 156 | UnwindData |  |
| 79 | `??1ofstream@@UEAA@XZ` | `0x6FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `?open@ofstream@@QEAAXPEBDHH@Z` | `0x7000` | 133 | UnwindData |  |
| 136 | `??6ostream@@QEAAAEAV0@E@Z` | `0x7090` | 195 | UnwindData |  |
| 144 | `??6ostream@@QEAAAEAV0@N@Z` | `0x7160` | 390 | UnwindData |  |
| 43 | `??0ostream@@IEAA@AEBV0@@Z` | `0x72F0` | 130 | UnwindData |  |
| 44 | `??0ostream@@IEAA@XZ` | `0x7380` | 63 | UnwindData |  |
| 45 | `??0ostream@@QEAA@PEAVstreambuf@@@Z` | `0x73D0` | 121 | UnwindData |  |
| 47 | `??0ostream_withassign@@QEAA@PEAVstreambuf@@@Z` | `0x7450` | 113 | UnwindData |  |
| 48 | `??0ostream_withassign@@QEAA@XZ` | `0x74D0` | 96 | UnwindData |  |
| 80 | `??1ostream@@UEAA@XZ` | `0x7540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??1ostream_withassign@@UEAA@XZ` | `0x7560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??4ostream@@IEAAAEAV0@PEAVstreambuf@@@Z` | `0x7590` | 184 | UnwindData |  |
| 150 | `??6ostream@@QEAAAEAV0@PEBD@Z` | `0x7650` | 65 | UnwindData |  |
| 253 | `?flush@ostream@@QEAAAEAV1@XZ` | `0x7740` | 163 | UnwindData |  |
| 296 | `?opfx@ostream@@QEAAHXZ` | `0x77F0` | 138 | UnwindData |  |
| 297 | `?osfx@ostream@@QEAAXXZ` | `0x7880` | 218 | UnwindData |  |
| 400 | `?writepad@ostream@@AEAAAEAV1@PEBD0@Z` | `0x7960` | 484 | UnwindData |  |
| 148 | `??6ostream@@QEAAAEAV0@PEAVstreambuf@@@Z` | `0x7B50` | 133 | UnwindData |  |
| 336 | `?seekp@ostream@@QEAAAEAV1@J@Z` | `0x7BE0` | 194 | UnwindData |  |
| 337 | `?seekp@ostream@@QEAAAEAV1@JW4seek_dir@ios@@@Z` | `0x7CB0` | 200 | UnwindData |  |
| 380 | `?tellp@ostream@@QEAAJXZ` | `0x7D80` | 208 | UnwindData |  |
| 139 | `??6ostream@@QEAAAEAV0@H@Z` | `0x7E60` | 251 | UnwindData |  |
| 145 | `??6ostream@@QEAAAEAV0@O@Z` | `0x7F70` | 387 | UnwindData |  |
| 141 | `??6ostream@@QEAAAEAV0@J@Z` | `0x8100` | 233 | UnwindData |  |
| 152 | `??6ostream@@QEAAAEAV0@PEBX@Z` | `0x81F0` | 199 | UnwindData |  |
| 314 | `?put@ostream@@QEAAAEAV1@E@Z` | `0x82C0` | 111 | UnwindData |  |
| 398 | `?write@ostream@@QEAAAEAV1@PEBDH@Z` | `0x8340` | 106 | UnwindData |  |
| 137 | `??6ostream@@QEAAAEAV0@F@Z` | `0x83B0` | 236 | UnwindData |  |
| 140 | `??6ostream@@QEAAAEAV0@I@Z` | `0x84B0` | 247 | UnwindData |  |
| 142 | `??6ostream@@QEAAAEAV0@K@Z` | `0x85B0` | 229 | UnwindData |  |
| 138 | `??6ostream@@QEAAAEAV0@G@Z` | `0x86A0` | 231 | UnwindData |  |
| 53 | `??0stdiobuf@@QEAA@PEAU_iobuf@@@Z` | `0x8790` | 59 | UnwindData |  |
| 55 | `??0stdiostream@@QEAA@PEAU_iobuf@@@Z` | `0x87E0` | 184 | UnwindData |  |
| 83 | `??1stdiobuf@@UEAA@XZ` | `0x88A0` | 46 | UnwindData |  |
| 84 | `??1stdiostream@@UEAA@XZ` | `0x88E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?overflow@stdiobuf@@UEAAHH@Z` | `0x8900` | 248 | UnwindData |  |
| 302 | `?pbackfail@stdiobuf@@UEAAHH@Z` | `0x8A00` | 121 | UnwindData |  |
| 333 | `?seekoff@stdiobuf@@UEAAJJW4seek_dir@ios@@H@Z` | `0x8A80` | 131 | UnwindData |  |
| 356 | `?setrwbuf@stdiobuf@@QEAAHHH@Z` | `0x8B10` | 228 | UnwindData |  |
| 375 | `?sync@stdiobuf@@UEAAHXZ` | `0x8C00` | 294 | UnwindData |  |
| 378 | `?sync_with_stdio@ios@@SAXXZ` | `0x8D30` | 671 | UnwindData |  |
| 387 | `?underflow@stdiobuf@@UEAAHXZ` | `0x8FE0` | 293 | UnwindData |  |
| 56 | `??0streambuf@@IEAA@PEADH@Z` | `0x9110` | 118 | UnwindData |  |
| 57 | `??0streambuf@@IEAA@XZ` | `0x9190` | 84 | UnwindData |  |
| 85 | `??1streambuf@@UEAA@XZ` | `0x91F0` | 54 | UnwindData |  |
| 204 | `?allocate@streambuf@@IEAAHXZ` | `0x9230` | 53 | UnwindData |  |
| 231 | `?doallocate@streambuf@@MEAAHXZ` | `0x9270` | 64 | UnwindData |  |
| 303 | `?pbackfail@streambuf@@UEAAHH@Z` | `0x92C0` | 130 | UnwindData |  |
| 334 | `?seekoff@streambuf@@UEAAJJW4seek_dir@ios@@H@Z` | `0x9350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `?seekpos@streambuf@@UEAAJJH@Z` | `0x9360` | 27 | UnwindData |  |
| 339 | `?setb@streambuf@@IEAAXPEAD0H@Z` | `0x9390` | 84 | UnwindData |  |
| 344 | `?setbuf@streambuf@@UEAAPEAV1@PEADH@Z` | `0x93F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?sync@streambuf@@UEAAHXZ` | `0x9430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?xsgetn@streambuf@@UEAAHPEADH@Z` | `0x9450` | 198 | UnwindData |  |
| 408 | `?xsputn@streambuf@@UEAAHPEBDH@Z` | `0x9520` | 123 | UnwindData |  |
| 329 | `?sbumpc@streambuf@@QEAAHXZ` | `0x95B0` | 83 | UnwindData |  |
| 357 | `?sgetc@streambuf@@QEAAHXZ` | `0x9610` | 62 | UnwindData |  |
| 362 | `?snextc@streambuf@@QEAAHXZ` | `0x9660` | 133 | UnwindData |  |
| 367 | `?stossc@streambuf@@QEAAXXZ` | `0x96F0` | 89 | UnwindData |  |
| 227 | `?dbp@streambuf@@QEAAXXZ` | `0x9750` | 254 | UnwindData |  |
| 33 | `??0istrstream@@QEAA@PEAD@Z` | `0x9860` | 164 | UnwindData |  |
| 34 | `??0istrstream@@QEAA@PEADH@Z` | `0x9910` | 176 | UnwindData |  |
| 50 | `??0ostrstream@@QEAA@PEADHH@Z` | `0x99D0` | 210 | UnwindData |  |
| 51 | `??0ostrstream@@QEAA@XZ` | `0x9AB0` | 156 | UnwindData |  |
| 60 | `??0strstream@@QEAA@PEADHH@Z` | `0x9B60` | 249 | UnwindData |  |
| 61 | `??0strstream@@QEAA@XZ` | `0x9C60` | 182 | UnwindData |  |
| 63 | `??0strstreambuf@@QEAA@H@Z` | `0x9D20` | 86 | UnwindData |  |
| 64 | `??0strstreambuf@@QEAA@P6APEAXJ@ZP6AXPEAX@Z@Z` | `0x9D80` | 96 | UnwindData |  |
| 65 | `??0strstreambuf@@QEAA@PEADH0@Z` | `0x9DF0` | 104 | UnwindData |  |
| 66 | `??0strstreambuf@@QEAA@PEAEH0@Z` | `0x9DF0` | 104 | UnwindData |  |
| 67 | `??0strstreambuf@@QEAA@XZ` | `0x9E60` | 72 | UnwindData |  |
| 77 | `??1istrstream@@UEAA@XZ` | `0x9EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??1ostrstream@@UEAA@XZ` | `0x9ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??1strstream@@UEAA@XZ` | `0x9EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??1strstreambuf@@UEAA@XZ` | `0x9F10` | 83 | UnwindData |  |
| 202 | `?_init@strstreambuf@@AEAAXPEADH0@Z` | `0x9F70` | 171 | UnwindData |  |
| 232 | `?doallocate@strstreambuf@@MEAAHXZ` | `0xA030` | 342 | UnwindData |  |
| 254 | `?freeze@strstreambuf@@QEAAXH@Z` | `0xA190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?overflow@strstreambuf@@UEAAHH@Z` | `0xA1B0` | 154 | UnwindData |  |
| 335 | `?seekoff@strstreambuf@@UEAAJJW4seek_dir@ios@@H@Z` | `0xA250` | 311 | UnwindData |  |
| 345 | `?setbuf@strstreambuf@@UEAAPEAVstreambuf@@PEADH@Z` | `0xA390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `?str@strstreambuf@@QEAAPEADXZ` | `0xA3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `?sync@strstreambuf@@UEAAHXZ` | `0xA3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `?underflow@strstreambuf@@UEAAHXZ` | `0xA3E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0exception@@QEAA@AEBQEBD@Z` | `0xA460` | 106 | UnwindData |  |
| 4 | `??0exception@@QEAA@AEBV0@@Z` | `0xA4D0` | 117 | UnwindData |  |
| 5 | `??0exception@@QEAA@XZ` | `0xA550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??0logic_error@@QEAA@$$QEAV0@@Z` | `0xA570` | 33 | UnwindData |  |
| 37 | `??0logic_error@@QEAA@AEBV0@@Z` | `0xA570` | 33 | UnwindData |  |
| 36 | `??0logic_error@@QEAA@AEBQEBD@Z` | `0xA5A0` | 33 | UnwindData |  |
| 69 | `??1exception@@UEAA@XZ` | `0xA5D0` | 34 | UnwindData |  |
| 78 | `??1logic_error@@UEAA@XZ` | `0xA600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `??4exception@@QEAAAEAV0@AEBV0@@Z` | `0xA610` | 51 | UnwindData |  |
| 102 | `??4logic_error@@QEAAAEAV0@$$QEAV0@@Z` | `0xA650` | 23 | UnwindData |  |
| 103 | `??4logic_error@@QEAAAEAV0@AEBV0@@Z` | `0xA650` | 23 | UnwindData |  |
| 394 | `?what@exception@@UEBAPEBDXZ` | `0xA770` | 10,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??_7streambuf@@6B@` | `0xD008` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??_7istream_withassign@@6B@` | `0xD068` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??_7ostream_withassign@@6B@` | `0xD078` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `??_7iostream@@6B@` | `0xD088` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??_7filebuf@@6B@` | `0xD098` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??_7ifstream@@6B@` | `0xD0F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `??_7ofstream@@6B@` | `0xD108` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??_7fstream@@6B@` | `0xD118` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??_7strstreambuf@@6B@` | `0xD128` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `??_7istrstream@@6B@` | `0xD188` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??_7ostrstream@@6B@` | `0xD198` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??_7strstream@@6B@` | `0xD1A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??_7stdiobuf@@6B@` | `0xD1B8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??_7stdiostream@@6B@` | `0xD218` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `??_7ios@@6B@` | `0xD228` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `??_7istream@@6B@` | `0xD238` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `??_7ostream@@6B@` | `0xD248` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `??_7exception@@6B@` | `0xD250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??_7logic_error@@6B@` | `0xD260` | 3,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `??_8istream_withassign@@7B@` | `0xE1E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??_8ostream_withassign@@7B@` | `0xE1F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `??_8iostream@@7Bistream@@@` | `0xE1F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `??_8iostream@@7Bostream@@@` | `0xE200` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??_8ifstream@@7B@` | `0xE208` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `??_8ofstream@@7B@` | `0xE210` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??_8fstream@@7Bistream@@@` | `0xE218` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??_8fstream@@7Bostream@@@` | `0xE220` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `??_8istrstream@@7B@` | `0xE228` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??_8ostrstream@@7B@` | `0xE230` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??_8strstream@@7Bistream@@@` | `0xE238` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??_8strstream@@7Bostream@@@` | `0xE240` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??_8stdiostream@@7Bistream@@@` | `0xE248` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??_8stdiostream@@7Bostream@@@` | `0xE250` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `?openprot@filebuf@@2HB` | `0xE2F8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `?sh_none@filebuf@@2HB` | `0xE2FC` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `?sh_read@filebuf@@2HB` | `0xE300` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `?sh_write@filebuf@@2HB` | `0xE304` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `?binary@filebuf@@2HB` | `0xE308` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `?text@filebuf@@2HB` | `0xE30C` | 404 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `?basefield@ios@@2JB` | `0xE4A0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?adjustfield@ios@@2JB` | `0xE4A4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `?floatfield@ios@@2JB` | `0xE4A8` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??_8istream@@7B@` | `0xE5C8` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `??_8ostream@@7B@` | `0xE798` | 31,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `?x_maxbit@ios@@0JA` | `0x16280` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?x_curindex@ios@@0HA` | `0x16284` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `__dummy_export` | `0x16290` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?cout@@3Vostream_withassign@@A` | `0x16320` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `?cerr@@3Vostream_withassign@@A` | `0x163B0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `?cin@@3Vistream_withassign@@A` | `0x16440` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?clog@@3Vostream_withassign@@A` | `0x164E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `?x_statebuf@ios@@0PAJA` | `0x16560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?fLockcInit@ios@@0HA` | `0x16580` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `?x_lockc@ios@@0U_CRT_CRITICAL_SECTION@@A` | `0x16588` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `?sunk_with_stdio@ios@@0HA` | `0x165B0` | 0 | Indeterminate |  |
