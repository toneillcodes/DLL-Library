# Binary Specification: oleaut32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oleaut32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d640055fe14afa8681415b80d7d185f5345867b430613355d27b7356ed564285`
* **Total Exported Functions:** 429

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 445 | `HWND_UserFree` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserFree` |
| 449 | `HWND_UserFree64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserFree64` |
| 446 | `HWND_UserMarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserMarshal` |
| 450 | `HWND_UserMarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserMarshal64` |
| 447 | `HWND_UserSize` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserSize` |
| 451 | `HWND_UserSize64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserSize64` |
| 448 | `HWND_UserUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserUnmarshal` |
| 452 | `HWND_UserUnmarshal64` | `0x0` | - | Forwarded | Forwarded to: `COMBASE.HWND_UserUnmarshal64` |
| 155 | `VarMod` | `0x1860` | 423 | UnwindData |  |
| 142 | `VarAnd` | `0x1A10` | 440 | UnwindData |  |
| 157 | `VarOr` | `0x1D20` | 421 | UnwindData |  |
| 107 | `VarFormatNumber` | `0x2030` | 287 | UnwindData |  |
| 176 | `VarCmp` | `0x26A0` | 4,153 | UnwindData |  |
| 314 | `VarBstrCmp` | `0x3770` | 228 | UnwindData |  |
| 7 | `SysStringLen` | `0x3990` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `VarFormatFromTokens` | `0x3AD0` | 8,596 | UnwindData |  |
| 185 | `VariantTimeToSystemTime` | `0x5E00` | 122 | UnwindData |  |
| 331 | `VarUdateFromDate` | `0x5E80` | 75 | UnwindData |  |
| 114 | `VarBstrFromDate` | `0x63E0` | 893 | UnwindData |  |
| 411 | `SafeArrayCreateVector` | `0x6910` | 957 | UnwindData |  |
| 184 | `SystemTimeToVariantTime` | `0x7B30` | 302 | UnwindData |  |
| 319 | `VarDateFromUdateEx` | `0x7C70` | 877 | UnwindData |  |
| 94 | `VarDateFromStr` | `0x8FE0` | 2,620 | UnwindData |  |
| 113 | `VarBstrFromCy` | `0x9A30` | 1,036 | UnwindData |  |
| 84 | `VarR8FromStr` | `0xA540` | 156 | UnwindData |  |
| 264 | `VarUI2FromStr` | `0xA640` | 58 | UnwindData |  |
| 277 | `VarUI4FromStr` | `0xAA10` | 152 | UnwindData |  |
| 64 | `VarI4FromStr` | `0xAAB0` | 340 | UnwindData |  |
| 46 | `VarParseNumFromStr` | `0xAC10` | 90 | UnwindData |  |
| 47 | `VarNumFromParseNum` | `0xC040` | 4,501 | UnwindData |  |
| 435 | `VarUI8FromStr` | `0xD4B0` | 154 | UnwindData |  |
| 231 | `VarBstrFromUI4` | `0xD550` | 209 | UnwindData |  |
| 109 | `VarBstrFromI2` | `0xD700` | 337 | UnwindData |  |
| 368 | `VarBstrFromI8` | `0xD860` | 180 | UnwindData |  |
| 125 | `VarBoolFromStr` | `0xD920` | 675 | UnwindData |  |
| 216 | `VarR4FromDec` | `0xDC40` | 165 | UnwindData |  |
| 12 | `VariantChangeType` | `0xDE40` | 31 | UnwindData |  |
| 147 | `VariantChangeTypeEx` | `0xDE70` | 127 | UnwindData |  |
| 25 | `SafeArrayGetElement` | `0x102D0` | 47 | UnwindData |  |
| 3 | `SysReAllocString` | `0x10570` | 24 | UnwindData |  |
| 26 | `SafeArrayPutElement` | `0x10790` | 47 | UnwindData |  |
| 150 | `SysAllocStringByteLen` | `0x10B50` | 76 | UnwindData |  |
| 4 | `SysAllocStringLen` | `0x10C10` | 89 | UnwindData |  |
| 2 | `SysAllocString` | `0x10CF0` | 18 | UnwindData |  |
| 5 | `SysReAllocStringLen` | `0x11000` | 458 | UnwindData |  |
| 285 | `BSTR_UserUnmarshal` | `0x12140` | 1,294 | UnwindData |  |
| 289 | `VARIANT_UserUnmarshal` | `0x13410` | 1,962 | UnwindData |  |
| 290 | `VARIANT_UserFree` | `0x13BC0` | 339 | UnwindData |  |
| 381 | `VARIANT_UserUnmarshal64` | `0x13D20` | 1,990 | UnwindData |  |
| 297 | `LPSAFEARRAY_Unmarshal` | `0x144F0` | 2,721 | UnwindData |  |
| 27 | `SafeArrayCopy` | `0x159C0` | 635 | UnwindData |  |
| 15 | `SafeArrayCreate` | `0x15C50` | 577 | UnwindData |  |
| 37 | `SafeArrayAllocData` | `0x15EA0` | 27 | UnwindData |  |
| 412 | `SafeArrayCopyData` | `0x16010` | 779 | UnwindData |  |
| 21 | `SafeArrayLock` | `0x16330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SafeArrayUnlock` | `0x16360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `LPSAFEARRAY_UserFree` | `0x16390` | 382 | UnwindData |  |
| 40 | `SafeArrayRedim` | `0x16890` | 1,258 | UnwindData |  |
| 286 | `BSTR_UserFree` | `0x16D80` | 37 | UnwindData |  |
| 144 | `BSTR_UserFree64` | `0x16D80` | 37 | UnwindData |  |
| 355 | `SafeArrayReleaseDescriptor` | `0x16E10` | 117 | UnwindData |  |
| 16 | `SafeArrayDestroy` | `0x175C0` | 1,568 | UnwindData |  |
| 357 | `SysReleaseString` | `0x18480` | 161 | UnwindData |  |
| 6 | `SysFreeString` | `0x18530` | 167 | UnwindData |  |
| 300 | `BSTR_UserUnmarshal64` | `0x18F70` | 343 | UnwindData |  |
| 323 | `GetRecordInfoFromTypeInfo` | `0x19D30` | 2,041 | UnwindData |  |
| 501 | *Ordinal Only* | `0x1BA50` | 710 | UnwindData |  |
| 164 | `QueryPathOfRegTypeLib` | `0x1BDC0` | 30 | UnwindData |  |
| 503 | *Ordinal Only* | `0x1BDF0` | 271 | UnwindData |  |
| 183 | `LoadTypeLibEx` | `0x1F470` | 1,244 | UnwindData |  |
| 162 | `LoadRegTypeLib` | `0x20400` | 38 | UnwindData |  |
| 180 | `CreateTypeLib2` | `0x29180` | 142 | UnwindData |  |
| 352 | `OACreateTypeLib2` | `0x29180` | 142 | UnwindData |  |
| 148 | `SafeArrayPtrOfIndex` | `0x29F60` | 40 | UnwindData |  |
| 351 | `LPSAFEARRAY_UserUnmarshal64` | `0x2AB80` | 2,550 | UnwindData |  |
| 42 | `SafeArrayCreateEx` | `0x2B5A0` | 325 | UnwindData |  |
| 41 | `SafeArrayAllocDescriptorEx` | `0x2B860` | 39 | UnwindData |  |
| 44 | `SafeArraySetRecordInfo` | `0x2B950` | 95 | UnwindData |  |
| 38 | `SafeArrayDestroyDescriptor` | `0x2B9C0` | 161 | UnwindData |  |
| 500 | `OACleanup` | `0x2BBD0` | 170 | UnwindData |  |
| 179 | `VarDecMul` | `0x2BD80` | 641 | UnwindData |  |
| 204 | `VarDecCmp` | `0x2C010` | 154 | UnwindData |  |
| 19 | `SafeArrayGetUBound` | `0x2C810` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `SafeArrayCreateVectorEx` | `0x2C880` | 922 | UnwindData |  |
| 413 | `VectorFromBstr` | `0x2CD80` | 113 | UnwindData |  |
| 149 | `SysStringByteLen` | `0x2CE00` | 14,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `LHashValOfNameSys` | `0x30790` | 150 | UnwindData |  |
| 166 | `LHashValOfNameSysA` | `0x31830` | 451 | UnwindData |  |
| 146 | `DispCallFunc` | `0x33850` | 942 | UnwindData |  |
| 20 | `SafeArrayGetLBound` | `0x33D10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `VARIANT_UserSize` | `0x33D50` | 959 | UnwindData |  |
| 295 | `LPSAFEARRAY_Size` | `0x34120` | 867 | UnwindData |  |
| 283 | `BSTR_UserSize` | `0x34490` | 87 | UnwindData |  |
| 23 | `SafeArrayAccessData` | `0x35D90` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SafeArrayGetDim` | `0x35EE0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SafeArrayUnaccessData` | `0x36060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `VarR8FromDec` | `0x36090` | 233 | UnwindData |  |
| 81 | `VarR8FromR4` | `0x36210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `VarDecInt` | `0x36230` | 51 | UnwindData |  |
| 187 | `VarDecFix` | `0x36270` | 26 | UnwindData |  |
| 203 | `VarDecRound` | `0x36350` | 277 | UnwindData |  |
| 110 | `VarBstrFromI4` | `0x36550` | 330 | UnwindData |  |
| 77 | `SafeArrayGetVartype` | `0x36990` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SafeArrayGetElemsize` | `0x369E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `VarDecFromR8` | `0x36A60` | 674 | UnwindData |  |
| 380 | `VARIANT_UserSize64` | `0x36FC0` | 876 | UnwindData |  |
| 151 | `BSTR_UserSize64` | `0x37340` | 87 | UnwindData |  |
| 302 | `DllGetClassObject` | `0x38190` | 339 | UnwindData |  |
| 141 | `VarAdd` | `0x38600` | 4,060 | UnwindData |  |
| 313 | `VarBstrCat` | `0x395F0` | 157 | UnwindData |  |
| 369 | `VarBstrFromUI8` | `0x3A030` | 312 | UnwindData |  |
| 193 | `VarDecFromR4` | `0x3A1A0` | 622 | UnwindData |  |
| 36 | `SafeArrayAllocDescriptor` | `0x3A640` | 136 | UnwindData |  |
| 111 | `VarBstrFromR4` | `0x3AFE0` | 288 | UnwindData |  |
| 112 | `VarBstrFromR8` | `0x3B110` | 288 | UnwindData |  |
| 143 | `VarDiv` | `0x3B5D0` | 3,012 | UnwindData |  |
| 57 | `SafeArraySetIID` | `0x3C1A0` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `VarTokenizeFormatString` | `0x3C9F0` | 708 | UnwindData |  |
| 116 | `VarBstrFromBool` | `0x3DC90` | 212 | UnwindData |  |
| 259 | `VarUI2FromI4` | `0x3DD70` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `VarUI2FromUI4` | `0x3DD70` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `VarBstrFromDec` | `0x3DF80` | 872 | UnwindData |  |
| 29 | `DispGetIDsOfNames` | `0x3E760` | 22 | UnwindData |  |
| 301 | `DllCanUnloadNow` | `0x3E7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `VarMul` | `0x3E7C0` | 3,591 | UnwindData |  |
| 251 | `VarI1FromStr` | `0x3F8A0` | 59 | UnwindData |  |
| 136 | `VarUI1FromStr` | `0x3F8F0` | 59 | UnwindData |  |
| 54 | `VarI2FromStr` | `0x3F940` | 154 | UnwindData |  |
| 130 | `VarUI1FromI2` | `0x3F9E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `VarUI1FromUI2` | `0x3F9E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `VarI8FromStr` | `0x3FD30` | 321 | UnwindData |  |
| 161 | `LoadTypeLib` | `0x3FE80` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `VarSub` | `0x40150` | 3,633 | UnwindData |  |
| 293 | `LPSAFEARRAY_UserUnmarshal` | `0x42290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `LPSAFEARRAY_UserSize` | `0x422A0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `VarI4FromR8` | `0x42880` | 50 | UnwindData |  |
| 432 | `VarUI8FromR8` | `0x42A60` | 57 | UnwindData |  |
| 292 | `LPSAFEARRAY_UserMarshal` | `0x42E30` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `VarUI4FromR8` | `0x42FF0` | 56 | UnwindData |  |
| 108 | `VarBstrFromUI1` | `0x432B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `VarCyFromBool` | `0x43320` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `VarCyFromI2` | `0x43320` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `VarBoolFromCy` | `0x433E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `VarUI4FromUI8` | `0x43460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `VarDecFromI2` | `0x43480` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `VarDecFromI4` | `0x43B50` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `VarBstrFromUI2` | `0x43F80` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `OleTranslateColor` | `0x443E0` | 76 | UnwindData |  |
| 419 | `OleCreatePictureIndirect` | `0x44480` | 94 | UnwindData |  |
| 241 | `VarDecFromI1` | `0x444F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `VarI4FromUI8` | `0x44520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `VarCyFromI4` | `0x44540` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DispInvoke` | `0x445E0` | 94 | UnwindData |  |
| 425 | `VarUI4FromI8` | `0x44B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `VarDecFromStr` | `0x44B50` | 161 | UnwindData |  |
| 414 | `BstrFromVector` | `0x44C00` | 97 | UnwindData |  |
| 72 | `VarR4FromCy` | `0x45340` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `VarR8FromCy` | `0x45540` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `VarI2FromUI4` | `0x45D50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `VarDecFromUI1` | `0x45DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `VarDecFromUI2` | `0x45DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `VarDecFromUI8` | `0x45E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `OleLoadPicture` | `0x45E30` | 39 | UnwindData |  |
| 401 | `OleLoadPictureEx` | `0x45E60` | 132 | UnwindData |  |
| 170 | `OaBuildVersion` | `0x45FF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `VarR4FromStr` | `0x46030` | 158 | UnwindData |  |
| 360 | `VarR4FromI8` | `0x460E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `VarCyFromUI1` | `0x46100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `VarDecFromUI4` | `0x46120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `VarCyFromI1` | `0x46140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `VarR4FromI1` | `0x46160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `VarR8FromI1` | `0x46180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `VarR4FromUI1` | `0x461A0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `VARIANT_UserFree64` | `0x46580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `RegisterTypeLib` | `0x46590` | 175 | UnwindData |  |
| 377 | `VarI1FromUI8` | `0x46F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `VarCyFromUI2` | `0x46F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `VarI2FromI4` | `0x46F60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `VarR4FromR8` | `0x46FC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `SafeArrayGetRecordInfo` | `0x47000` | 59 | UnwindData |  |
| 336 | `VarI8FromR8` | `0x47160` | 51 | UnwindData |  |
| 205 | `VarI2FromI1` | `0x471F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `VarI4FromI1` | `0x47200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `VarI8FromI1` | `0x47210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `RegisterActiveObject` | `0x47230` | 94 | UnwindData |  |
| 227 | `VarCyFromUI4` | `0x47460` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `VarDateFromUI1` | `0x474E0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `VarR8FromUI1` | `0x474E0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `VarI4FromI8` | `0x47670` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `GetAltMonthNames` | `0x47870` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SafeArrayGetIID` | `0x479A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `VarDateFromUdate` | `0x47A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `VarCyFromR4` | `0x47A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `VarI1FromR4` | `0x47A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `VarI2FromR4` | `0x47A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `VarI4FromR4` | `0x47A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `VarI8FromR4` | `0x47A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `VarUI1FromR4` | `0x47A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `VarUI2FromR4` | `0x47A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `VarUI4FromR4` | `0x47AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `VarUI8FromR4` | `0x47AB0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `VarBstrFromI1` | `0x47C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `SafeArrayDestroyData` | `0x47C10` | 84 | UnwindData |  |
| 324 | `LPSAFEARRAY_UserFree64` | `0x47ED0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `VarDecDiv` | `0x47F60` | 1,714 | UnwindData |  |
| 131 | `VarUI1FromI4` | `0x48880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `VarUI1FromUI4` | `0x48880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DosDateTimeToVariantTime` | `0x488A0` | 272 | UnwindData |  |
| 34 | `RevokeActiveObject` | `0x489C0` | 60 | UnwindData |  |
| 172 | `VarInt` | `0x48A30` | 485 | UnwindData |  |
| 103 | `VarCyFromDate` | `0x48C20` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `VarCyFromR8` | `0x48C20` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `OleCreateFontIndirect` | `0x48E70` | 78 | UnwindData |  |
| 327 | `SetOaNoCache` | `0x491F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `VarNot` | `0x492A0` | 159 | UnwindData |  |
| 271 | `VarUI4FromI2` | `0x49390` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `VarI4FromDec` | `0x493F0` | 179 | UnwindData |  |
| 51 | `VarI2FromR8` | `0x49540` | 51 | UnwindData |  |
| 356 | `SysAddRefString` | `0x49600` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `VarFormat` | `0x497C0` | 231 | UnwindData |  |
| 284 | `BSTR_UserMarshal` | `0x49D30` | 132 | UnwindData |  |
| 145 | `BSTR_UserMarshal64` | `0x49DC0` | 138 | UnwindData |  |
| 296 | `LPSAFEARRAY_Marshal` | `0x49F00` | 1,158 | UnwindData |  |
| 328 | `LPSAFEARRAY_UserMarshal64` | `0x4A390` | 1,233 | UnwindData |  |
| 350 | `LPSAFEARRAY_UserSize64` | `0x4A870` | 897 | UnwindData |  |
| 288 | `VARIANT_UserMarshal` | `0x4AC00` | 995 | UnwindData |  |
| 359 | `VARIANT_UserMarshal64` | `0x4AFF0` | 1,022 | UnwindData |  |
| 263 | `VarUI2FromCy` | `0x4B820` | 47 | UnwindData |  |
| 134 | `VarUI1FromCy` | `0x4B860` | 70 | UnwindData |  |
| 52 | `VarI2FromCy` | `0x4B8B0` | 66 | UnwindData |  |
| 250 | `VarI1FromCy` | `0x4B900` | 70 | UnwindData |  |
| 62 | `VarI4FromCy` | `0x4B950` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `VarCyFromStr` | `0x4C2E0` | 154 | UnwindData |  |
| 304 | `VarCyMulI4` | `0x4C760` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `VarI8FromCy` | `0x4C830` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `VarCyFromDec` | `0x4C980` | 896 | UnwindData |  |
| 32 | `CreateStdDispatch` | `0x4D2B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `VarDecFromI8` | `0x4D2F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `VarUI1FromDec` | `0x4D340` | 162 | UnwindData |  |
| 269 | `VarUI2FromDec` | `0x4D3F0` | 163 | UnwindData |  |
| 441 | `VarUI8FromDec` | `0x4D4A0` | 172 | UnwindData |  |
| 256 | `VarI1FromDec` | `0x4D560` | 172 | UnwindData |  |
| 208 | `VarI2FromDec` | `0x4D620` | 173 | UnwindData |  |
| 345 | `VarI8FromDec` | `0x4D6E0` | 197 | UnwindData |  |
| 282 | `VarUI4FromDec` | `0x4D7E0` | 157 | UnwindData |  |
| 224 | `VarDateFromDec` | `0x4D8B0` | 141 | UnwindData |  |
| 196 | `VarDecFromCy` | `0x4DA20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `VarCyFromI8` | `0x4DAA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `VarI1FromI2` | `0x4DAE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `VarUI2FromI1` | `0x4DB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `VarUI4FromI1` | `0x4DB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `VarUI8FromI1` | `0x4DB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `VarUI8FromI2` | `0x4DBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `VarI1FromI4` | `0x4DBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `VarI1FromI8` | `0x4DBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `VarI2FromI8` | `0x4DC10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `VarI1FromUI2` | `0x4DC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `VarI1FromUI4` | `0x4DC60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `VarDateFromCy` | `0x4DC90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `VarDateFromBool` | `0x4DCD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `VarDateFromI2` | `0x4DCD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `VarR8FromBool` | `0x4DCD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `VarR8FromI2` | `0x4DCD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `VarBoolFromDec` | `0x4DD30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `VarI1FromR8` | `0x4DD60` | 50 | UnwindData |  |
| 133 | `VarUI1FromR8` | `0x4DDA0` | 50 | UnwindData |  |
| 261 | `VarUI2FromR8` | `0x4DDE0` | 51 | UnwindData |  |
| 311 | `VarCyCmp` | `0x4DE20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `VarUI4FromCy` | `0x4DE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `VarUI8FromCy` | `0x4DEA0` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CreateErrorInfo` | `0x4F400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `GetErrorInfo` | `0x4F410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `SetErrorInfo` | `0x4F420` | 37,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CreateTypeLib` | `0x58670` | 170 | UnwindData |  |
| 186 | `UnRegisterTypeLib` | `0x58CE0` | 141 | UnwindData |  |
| 443 | `UnRegisterTypeLibForUser` | `0x58D80` | 173 | UnwindData |  |
| 504 | *Ordinal Only* | `0x5A3C0` | 44 | UnwindData |  |
| 442 | `RegisterTypeLibForUser` | `0x5A4D0` | 132 | UnwindData |  |
| 502 | *Ordinal Only* | `0x5AEF0` | 385 | UnwindData |  |
| 326 | `GetVarConversionLocaleSetting` | `0x5B080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `OaEnablePerUserTLibRegistration` | `0x5B0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `SetVarConversionLocaleSetting` | `0x5B0D0` | 167 | UnwindData |  |
| 171 | `ClearCustData` | `0x6FB20` | 142 | UnwindData |  |
| 168 | `VarAbs` | `0x726D0` | 617 | UnwindData |  |
| 310 | `VarCyRound` | `0x72940` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `VarFix` | `0x729D0` | 508 | UnwindData |  |
| 173 | `VarNeg` | `0x72BE0` | 678 | UnwindData |  |
| 317 | `VarR8Round` | `0x72E90` | 226 | UnwindData |  |
| 175 | `VarRound` | `0x72F80` | 519 | UnwindData |  |
| 318 | `VarCat` | `0x73340` | 205 | UnwindData |  |
| 329 | `VarCyMulI8` | `0x73420` | 122 | UnwindData |  |
| 158 | `VarPow` | `0x734A0` | 360 | UnwindData |  |
| 315 | `VarR8Pow` | `0x73610` | 210 | UnwindData |  |
| 152 | `VarEqv` | `0x736F0` | 42 | UnwindData |  |
| 153 | `VarIdiv` | `0x73720` | 488 | UnwindData |  |
| 154 | `VarImp` | `0x73910` | 253 | UnwindData |  |
| 167 | `VarXor` | `0x73A20` | 356 | UnwindData |  |
| 298 | `VarDecCmpR8` | `0x73B90` | 114 | UnwindData |  |
| 316 | `VarR4CmpR8` | `0x73C10` | 67 | UnwindData |  |
| 306 | `VarCyAbs` | `0x73C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `VarCyAdd` | `0x73C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `VarCyCmpR8` | `0x73CC0` | 95 | UnwindData |  |
| 307 | `VarCyFix` | `0x73D30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `VarCyInt` | `0x73D70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `VarCyMul` | `0x73DE0` | 317 | UnwindData |  |
| 309 | `VarCyNeg` | `0x73F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `VarCySub` | `0x73F60` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `VarDecAbs` | `0x74340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `VarDecAdd` | `0x74370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `VarDecNeg` | `0x74380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `VarDecSub` | `0x743B0` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `VarBoolFromDate` | `0x74A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `VarBoolFromDisp` | `0x74A50` | 57 | UnwindData |  |
| 233 | `VarBoolFromI1` | `0x74A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `VarBoolFromUI1` | `0x74A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `VarBoolFromI2` | `0x74AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `VarBoolFromUI2` | `0x74AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `VarBoolFromI4` | `0x74AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `VarBoolFromUI4` | `0x74AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `VarBoolFromI8` | `0x74AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `VarBoolFromUI8` | `0x74AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `VarBoolFromR4` | `0x74B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `VarBoolFromR8` | `0x74B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `VarBstrFromDisp` | `0x74B50` | 57 | UnwindData |  |
| 105 | `VarCyFromDisp` | `0x74B90` | 57 | UnwindData |  |
| 367 | `VarCyFromUI8` | `0x74BD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `VarDateFromDisp` | `0x74C00` | 59 | UnwindData |  |
| 221 | `VarDateFromI1` | `0x74C50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `VarDateFromI4` | `0x74C90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `VarDateFromI8` | `0x74CD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `VarDateFromR4` | `0x74D10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `VarDateFromR8` | `0x74D40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `VarDateFromUI2` | `0x74D70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `VarDateFromUI4` | `0x74DB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `VarDateFromUI8` | `0x74DF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `VarI1FromBool` | `0x74E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `VarUI1FromBool` | `0x74E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `VarI1FromDate` | `0x74E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `VarI1FromDisp` | `0x74E70` | 55 | UnwindData |  |
| 244 | `VarI1FromUI1` | `0x74EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `VarI2FromBool` | `0x74ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `VarUI2FromBool` | `0x74ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `VarI2FromDate` | `0x74EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `VarI2FromDisp` | `0x74EF0` | 57 | UnwindData |  |
| 48 | `VarI2FromUI1` | `0x74F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `VarUI2FromUI1` | `0x74F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `VarI2FromUI2` | `0x74F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `VarI2FromUI8` | `0x74F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `VarI4FromBool` | `0x74F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `VarI4FromI2` | `0x74F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `VarUI4FromBool` | `0x74F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `VarI4FromDate` | `0x74F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `VarI4FromDisp` | `0x74FA0` | 55 | UnwindData |  |
| 58 | `VarI4FromUI1` | `0x74FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `VarUI4FromUI1` | `0x74FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `VarI4FromUI2` | `0x74FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `VarUI4FromUI2` | `0x74FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `VarI4FromUI4` | `0x75000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `VarI8FromBool` | `0x75020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `VarI8FromI2` | `0x75020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `VarUI8FromBool` | `0x75020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `VarI8FromDate` | `0x75040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `VarI8FromDisp` | `0x75050` | 57 | UnwindData |  |
| 333 | `VarI8FromUI1` | `0x75090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `VarUI8FromUI1` | `0x75090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `VarI8FromUI2` | `0x750A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `VarUI8FromUI2` | `0x750A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `VarI8FromUI4` | `0x750B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `VarUI8FromUI4` | `0x750B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `VarI8FromUI8` | `0x750C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `VarR4FromBool` | `0x750F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `VarR4FromI2` | `0x750F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `VarR4FromDate` | `0x75110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `VarR4FromDisp` | `0x75120` | 59 | UnwindData |  |
| 70 | `VarR4FromI4` | `0x75170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `VarR4FromUI2` | `0x75190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `VarR4FromUI4` | `0x751B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `VarR4FromUI8` | `0x751D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `VarR8FromDate` | `0x75210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `VarR8FromDisp` | `0x75220` | 59 | UnwindData |  |
| 80 | `VarR8FromI4` | `0x75270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `VarR8FromI8` | `0x75290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `VarR8FromUI2` | `0x752B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `VarR8FromUI4` | `0x752D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `VarR8FromUI8` | `0x752F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `VarUI1FromDate` | `0x75330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `VarUI1FromDisp` | `0x75340` | 55 | UnwindData |  |
| 237 | `VarUI1FromI1` | `0x75380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `VarUI1FromI8` | `0x753A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `VarUI1FromUI8` | `0x753A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `VarUI2FromDate` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `VarUI2FromDisp` | `0x753D0` | 57 | UnwindData |  |
| 258 | `VarUI2FromI2` | `0x75410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `VarUI2FromI8` | `0x75430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `VarUI2FromUI8` | `0x75430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `VarUI4FromDate` | `0x75450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `VarUI4FromDisp` | `0x75460` | 55 | UnwindData |  |
| 272 | `VarUI4FromI4` | `0x754A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `VarUI8FromDate` | `0x754C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `VarUI8FromDisp` | `0x754D0` | 57 | UnwindData |  |
| 428 | `VarUI8FromI8` | `0x75510` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `CreateDispTypeInfo` | `0x75940` | 58 | UnwindData |  |
| 28 | `DispGetParam` | `0x759A0` | 123 | UnwindData |  |
| 320 | `DllRegisterServer` | `0x76130` | 839 | UnwindData |  |
| 321 | `DllUnregisterServer` | `0x76480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `VariantTimeToDosDateTime` | `0x76490` | 180 | UnwindData |  |
| 35 | `GetActiveObject` | `0x76550` | 78 | UnwindData |  |
| 322 | `GetRecordInfoFromGuids` | `0x798B0` | 376 | UnwindData |  |
| 417 | `OleCreatePropertyFrame` | `0x79EC0` | 94 | UnwindData |  |
| 416 | `OleCreatePropertyFrameIndirect` | `0x79F30` | 50 | UnwindData |  |
| 415 | `OleIconToCursor` | `0x79F70` | 76 | UnwindData |  |
| 422 | `OleLoadPictureFile` | `0x79FD0` | 51 | UnwindData |  |
| 402 | `OleLoadPictureFileEx` | `0x7A010` | 126 | UnwindData |  |
| 424 | `OleLoadPicturePath` | `0x7A0A0` | 114 | UnwindData |  |
| 423 | `OleSavePictureFile` | `0x7A120` | 62 | UnwindData |  |
| 353 | `SafeArrayAddRef` | `0x7A2E0` | 124 | UnwindData |  |
| 354 | `SafeArrayReleaseData` | `0x7A370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `VarDecFromBool` | `0x7A3B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `VarDecFromDate` | `0x7A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `VarDecFromDisp` | `0x7A3F0` | 68 | UnwindData |  |
| 127 | `VarFormatCurrency` | `0x7B730` | 282 | UnwindData |  |
| 97 | `VarFormatDateTime` | `0x7B850` | 129 | UnwindData |  |
| 117 | `VarFormatPercent` | `0x7B8E0` | 247 | UnwindData |  |
| 129 | `VarMonthName` | `0x7B9E0` | 195 | UnwindData |  |
| 128 | `VarWeekdayName` | `0x7BAB0` | 240 | UnwindData |  |
| 11 | `VariantCopyInd` | `0xA0120` | 661 | UnwindData |  |
| 10 | `VariantCopy` | `0xA03C0` | 41 | UnwindData |  |
| 9 | `VariantClear` | `0xA06A0` | 581 | UnwindData |  |
| 8 | `VariantInit` | `0xA08F0` | 0 | Indeterminate |  |
