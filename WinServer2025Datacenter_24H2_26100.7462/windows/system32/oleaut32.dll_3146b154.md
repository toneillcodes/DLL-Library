# Binary Specification: oleaut32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\oleaut32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3146b15435de6c26ffa43f0626f87ab5d05f612eaa0a22d059006cd28f84aa71`
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
| 155 | `VarMod` | `0x1850` | 423 | UnwindData |  |
| 142 | `VarAnd` | `0x1A00` | 440 | UnwindData |  |
| 157 | `VarOr` | `0x1D10` | 421 | UnwindData |  |
| 107 | `VarFormatNumber` | `0x2020` | 287 | UnwindData |  |
| 176 | `VarCmp` | `0x2690` | 4,153 | UnwindData |  |
| 314 | `VarBstrCmp` | `0x3760` | 228 | UnwindData |  |
| 7 | `SysStringLen` | `0x3980` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `VarFormatFromTokens` | `0x3AC0` | 8,596 | UnwindData |  |
| 185 | `VariantTimeToSystemTime` | `0x5DF0` | 122 | UnwindData |  |
| 331 | `VarUdateFromDate` | `0x5E70` | 75 | UnwindData |  |
| 114 | `VarBstrFromDate` | `0x63D0` | 893 | UnwindData |  |
| 411 | `SafeArrayCreateVector` | `0x6900` | 957 | UnwindData |  |
| 184 | `SystemTimeToVariantTime` | `0x7B20` | 302 | UnwindData |  |
| 319 | `VarDateFromUdateEx` | `0x7C60` | 877 | UnwindData |  |
| 94 | `VarDateFromStr` | `0x8FD0` | 2,620 | UnwindData |  |
| 113 | `VarBstrFromCy` | `0x9A20` | 1,036 | UnwindData |  |
| 84 | `VarR8FromStr` | `0xA530` | 156 | UnwindData |  |
| 264 | `VarUI2FromStr` | `0xA630` | 58 | UnwindData |  |
| 277 | `VarUI4FromStr` | `0xAA00` | 152 | UnwindData |  |
| 64 | `VarI4FromStr` | `0xAAA0` | 340 | UnwindData |  |
| 46 | `VarParseNumFromStr` | `0xAC00` | 90 | UnwindData |  |
| 47 | `VarNumFromParseNum` | `0xC030` | 4,501 | UnwindData |  |
| 435 | `VarUI8FromStr` | `0xD4A0` | 154 | UnwindData |  |
| 231 | `VarBstrFromUI4` | `0xD540` | 209 | UnwindData |  |
| 109 | `VarBstrFromI2` | `0xD6F0` | 337 | UnwindData |  |
| 368 | `VarBstrFromI8` | `0xD850` | 180 | UnwindData |  |
| 125 | `VarBoolFromStr` | `0xD910` | 675 | UnwindData |  |
| 216 | `VarR4FromDec` | `0xDC30` | 165 | UnwindData |  |
| 12 | `VariantChangeType` | `0xDE30` | 31 | UnwindData |  |
| 147 | `VariantChangeTypeEx` | `0xDE60` | 127 | UnwindData |  |
| 25 | `SafeArrayGetElement` | `0x102C0` | 47 | UnwindData |  |
| 3 | `SysReAllocString` | `0x10560` | 24 | UnwindData |  |
| 26 | `SafeArrayPutElement` | `0x10780` | 47 | UnwindData |  |
| 150 | `SysAllocStringByteLen` | `0x10B40` | 76 | UnwindData |  |
| 4 | `SysAllocStringLen` | `0x10C00` | 89 | UnwindData |  |
| 2 | `SysAllocString` | `0x10CE0` | 18 | UnwindData |  |
| 5 | `SysReAllocStringLen` | `0x10FF0` | 458 | UnwindData |  |
| 285 | `BSTR_UserUnmarshal` | `0x125E0` | 1,294 | UnwindData |  |
| 289 | `VARIANT_UserUnmarshal` | `0x138B0` | 1,962 | UnwindData |  |
| 290 | `VARIANT_UserFree` | `0x14060` | 339 | UnwindData |  |
| 381 | `VARIANT_UserUnmarshal64` | `0x141C0` | 1,990 | UnwindData |  |
| 297 | `LPSAFEARRAY_Unmarshal` | `0x14990` | 2,721 | UnwindData |  |
| 27 | `SafeArrayCopy` | `0x15E60` | 635 | UnwindData |  |
| 15 | `SafeArrayCreate` | `0x160F0` | 577 | UnwindData |  |
| 37 | `SafeArrayAllocData` | `0x16340` | 27 | UnwindData |  |
| 412 | `SafeArrayCopyData` | `0x164B0` | 779 | UnwindData |  |
| 21 | `SafeArrayLock` | `0x167D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SafeArrayUnlock` | `0x16800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `LPSAFEARRAY_UserFree` | `0x16830` | 382 | UnwindData |  |
| 40 | `SafeArrayRedim` | `0x16D30` | 1,258 | UnwindData |  |
| 286 | `BSTR_UserFree` | `0x17220` | 37 | UnwindData |  |
| 144 | `BSTR_UserFree64` | `0x17220` | 37 | UnwindData |  |
| 355 | `SafeArrayReleaseDescriptor` | `0x172B0` | 117 | UnwindData |  |
| 16 | `SafeArrayDestroy` | `0x17A60` | 1,568 | UnwindData |  |
| 357 | `SysReleaseString` | `0x18920` | 161 | UnwindData |  |
| 6 | `SysFreeString` | `0x189D0` | 167 | UnwindData |  |
| 300 | `BSTR_UserUnmarshal64` | `0x19450` | 343 | UnwindData |  |
| 323 | `GetRecordInfoFromTypeInfo` | `0x1A210` | 2,041 | UnwindData |  |
| 501 | *Ordinal Only* | `0x1BF30` | 710 | UnwindData |  |
| 164 | `QueryPathOfRegTypeLib` | `0x1C2A0` | 30 | UnwindData |  |
| 503 | *Ordinal Only* | `0x1C2D0` | 271 | UnwindData |  |
| 183 | `LoadTypeLibEx` | `0x1F930` | 1,244 | UnwindData |  |
| 162 | `LoadRegTypeLib` | `0x208C0` | 38 | UnwindData |  |
| 180 | `CreateTypeLib2` | `0x295F0` | 142 | UnwindData |  |
| 352 | `OACreateTypeLib2` | `0x295F0` | 142 | UnwindData |  |
| 148 | `SafeArrayPtrOfIndex` | `0x2A3D0` | 40 | UnwindData |  |
| 351 | `LPSAFEARRAY_UserUnmarshal64` | `0x2AFF0` | 2,550 | UnwindData |  |
| 42 | `SafeArrayCreateEx` | `0x2BA10` | 325 | UnwindData |  |
| 41 | `SafeArrayAllocDescriptorEx` | `0x2BCD0` | 39 | UnwindData |  |
| 44 | `SafeArraySetRecordInfo` | `0x2BDC0` | 95 | UnwindData |  |
| 38 | `SafeArrayDestroyDescriptor` | `0x2BE30` | 161 | UnwindData |  |
| 500 | `OACleanup` | `0x2C040` | 170 | UnwindData |  |
| 179 | `VarDecMul` | `0x2C1F0` | 641 | UnwindData |  |
| 204 | `VarDecCmp` | `0x2C480` | 154 | UnwindData |  |
| 165 | `LHashValOfNameSys` | `0x2F3B0` | 150 | UnwindData |  |
| 166 | `LHashValOfNameSysA` | `0x30450` | 451 | UnwindData |  |
| 19 | `SafeArrayGetUBound` | `0x32950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `SafeArrayCreateVectorEx` | `0x329C0` | 922 | UnwindData |  |
| 413 | `VectorFromBstr` | `0x32EC0` | 113 | UnwindData |  |
| 149 | `SysStringByteLen` | `0x32F40` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `DispCallFunc` | `0x334E0` | 942 | UnwindData |  |
| 20 | `SafeArrayGetLBound` | `0x339A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `VARIANT_UserSize` | `0x339E0` | 959 | UnwindData |  |
| 295 | `LPSAFEARRAY_Size` | `0x33DB0` | 867 | UnwindData |  |
| 283 | `BSTR_UserSize` | `0x34120` | 87 | UnwindData |  |
| 23 | `SafeArrayAccessData` | `0x35A20` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SafeArrayGetDim` | `0x35B70` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SafeArrayUnaccessData` | `0x35CF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `VarR8FromDec` | `0x35D20` | 233 | UnwindData |  |
| 81 | `VarR8FromR4` | `0x35EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `VarDecInt` | `0x35EC0` | 51 | UnwindData |  |
| 187 | `VarDecFix` | `0x35F00` | 26 | UnwindData |  |
| 203 | `VarDecRound` | `0x35FE0` | 277 | UnwindData |  |
| 110 | `VarBstrFromI4` | `0x361E0` | 330 | UnwindData |  |
| 77 | `SafeArrayGetVartype` | `0x36620` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SafeArrayGetElemsize` | `0x36670` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `VarDecFromR8` | `0x366F0` | 674 | UnwindData |  |
| 380 | `VARIANT_UserSize64` | `0x36C50` | 876 | UnwindData |  |
| 151 | `BSTR_UserSize64` | `0x36FD0` | 87 | UnwindData |  |
| 302 | `DllGetClassObject` | `0x38130` | 339 | UnwindData |  |
| 141 | `VarAdd` | `0x38570` | 4,060 | UnwindData |  |
| 313 | `VarBstrCat` | `0x39560` | 157 | UnwindData |  |
| 369 | `VarBstrFromUI8` | `0x39FA0` | 312 | UnwindData |  |
| 193 | `VarDecFromR4` | `0x3A110` | 622 | UnwindData |  |
| 36 | `SafeArrayAllocDescriptor` | `0x3A5B0` | 136 | UnwindData |  |
| 111 | `VarBstrFromR4` | `0x3B2D0` | 288 | UnwindData |  |
| 112 | `VarBstrFromR8` | `0x3B400` | 288 | UnwindData |  |
| 143 | `VarDiv` | `0x3B8C0` | 3,012 | UnwindData |  |
| 57 | `SafeArraySetIID` | `0x3C490` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `VarTokenizeFormatString` | `0x3CCE0` | 708 | UnwindData |  |
| 116 | `VarBstrFromBool` | `0x3DF80` | 212 | UnwindData |  |
| 259 | `VarUI2FromI4` | `0x3E060` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `VarUI2FromUI4` | `0x3E060` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `VarBstrFromDec` | `0x3E270` | 872 | UnwindData |  |
| 29 | `DispGetIDsOfNames` | `0x3EA50` | 22 | UnwindData |  |
| 301 | `DllCanUnloadNow` | `0x3EAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `VarMul` | `0x3EAB0` | 3,591 | UnwindData |  |
| 251 | `VarI1FromStr` | `0x3FB90` | 59 | UnwindData |  |
| 136 | `VarUI1FromStr` | `0x3FBE0` | 59 | UnwindData |  |
| 54 | `VarI2FromStr` | `0x3FC30` | 154 | UnwindData |  |
| 130 | `VarUI1FromI2` | `0x3FCD0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `VarUI1FromUI2` | `0x3FCD0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `VarI8FromStr` | `0x40020` | 321 | UnwindData |  |
| 161 | `LoadTypeLib` | `0x40170` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `VarSub` | `0x40440` | 3,633 | UnwindData |  |
| 293 | `LPSAFEARRAY_UserUnmarshal` | `0x42580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `LPSAFEARRAY_UserSize` | `0x42590` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `VarI4FromR8` | `0x42AD0` | 50 | UnwindData |  |
| 432 | `VarUI8FromR8` | `0x42CB0` | 57 | UnwindData |  |
| 292 | `LPSAFEARRAY_UserMarshal` | `0x43080` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `VarUI4FromR8` | `0x43240` | 56 | UnwindData |  |
| 108 | `VarBstrFromUI1` | `0x43500` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `VarCyFromBool` | `0x43570` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `VarCyFromI2` | `0x43570` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `VarBoolFromCy` | `0x43630` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `VarUI4FromUI8` | `0x436B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `VarDecFromI2` | `0x436D0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `VarDecFromI4` | `0x43E20` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `VarBstrFromUI2` | `0x44250` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `OleTranslateColor` | `0x446B0` | 76 | UnwindData |  |
| 419 | `OleCreatePictureIndirect` | `0x44750` | 94 | UnwindData |  |
| 241 | `VarDecFromI1` | `0x447C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `VarI4FromUI8` | `0x447F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `VarCyFromI4` | `0x44810` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DispInvoke` | `0x448B0` | 94 | UnwindData |  |
| 425 | `VarUI4FromI8` | `0x44E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `VarDecFromStr` | `0x44E20` | 161 | UnwindData |  |
| 414 | `BstrFromVector` | `0x44ED0` | 97 | UnwindData |  |
| 72 | `VarR4FromCy` | `0x45760` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `VarR8FromCy` | `0x45960` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `VarI2FromUI4` | `0x46170` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `VarDecFromUI1` | `0x461F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `VarDecFromUI2` | `0x46210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `VarDecFromUI8` | `0x46230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `OleLoadPicture` | `0x46250` | 39 | UnwindData |  |
| 401 | `OleLoadPictureEx` | `0x46280` | 132 | UnwindData |  |
| 170 | `OaBuildVersion` | `0x465B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `VarR4FromStr` | `0x465F0` | 158 | UnwindData |  |
| 360 | `VarR4FromI8` | `0x466A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `VarCyFromUI1` | `0x466C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `VarDecFromUI4` | `0x466E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `VarCyFromI1` | `0x46700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `VarR4FromI1` | `0x46720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `VarR8FromI1` | `0x46740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `VarR4FromUI1` | `0x46760` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `VARIANT_UserFree64` | `0x469F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `RegisterTypeLib` | `0x46A00` | 175 | UnwindData |  |
| 377 | `VarI1FromUI8` | `0x47390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `VarCyFromUI2` | `0x473B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `VarI2FromI4` | `0x473D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `VarR4FromR8` | `0x47430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `SafeArrayGetRecordInfo` | `0x47470` | 59 | UnwindData |  |
| 336 | `VarI8FromR8` | `0x475D0` | 51 | UnwindData |  |
| 205 | `VarI2FromI1` | `0x47660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `VarI4FromI1` | `0x47670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `VarI8FromI1` | `0x47680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `RegisterActiveObject` | `0x476A0` | 94 | UnwindData |  |
| 227 | `VarCyFromUI4` | `0x478D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `VarDateFromUI1` | `0x478F0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `VarR8FromUI1` | `0x478F0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `VarI4FromI8` | `0x47A80` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `GetAltMonthNames` | `0x47B80` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SafeArrayGetIID` | `0x47CB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `VarDateFromUdate` | `0x47D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `VarCyFromR4` | `0x47D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `VarI1FromR4` | `0x47D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `VarI2FromR4` | `0x47D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `VarI4FromR4` | `0x47D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `VarI8FromR4` | `0x47D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `VarUI1FromR4` | `0x47D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `VarUI2FromR4` | `0x47DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `VarUI4FromR4` | `0x47DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `VarUI8FromR4` | `0x47DC0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `VarBstrFromI1` | `0x47ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `SafeArrayDestroyData` | `0x47EE0` | 84 | UnwindData |  |
| 324 | `LPSAFEARRAY_UserFree64` | `0x48220` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `VarDecDiv` | `0x482B0` | 1,714 | UnwindData |  |
| 131 | `VarUI1FromI4` | `0x48B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `VarUI1FromUI4` | `0x48B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DosDateTimeToVariantTime` | `0x48B50` | 272 | UnwindData |  |
| 34 | `RevokeActiveObject` | `0x48C70` | 60 | UnwindData |  |
| 172 | `VarInt` | `0x48CE0` | 485 | UnwindData |  |
| 103 | `VarCyFromDate` | `0x48ED0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `VarCyFromR8` | `0x48ED0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `OleCreateFontIndirect` | `0x49120` | 78 | UnwindData |  |
| 327 | `SetOaNoCache` | `0x494A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `VarNot` | `0x49580` | 159 | UnwindData |  |
| 271 | `VarUI4FromI2` | `0x49670` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `VarI4FromDec` | `0x496D0` | 179 | UnwindData |  |
| 51 | `VarI2FromR8` | `0x49820` | 51 | UnwindData |  |
| 356 | `SysAddRefString` | `0x498E0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `VarFormat` | `0x49AA0` | 231 | UnwindData |  |
| 284 | `BSTR_UserMarshal` | `0x49F90` | 132 | UnwindData |  |
| 145 | `BSTR_UserMarshal64` | `0x4A020` | 138 | UnwindData |  |
| 296 | `LPSAFEARRAY_Marshal` | `0x4A160` | 1,158 | UnwindData |  |
| 328 | `LPSAFEARRAY_UserMarshal64` | `0x4A5F0` | 1,233 | UnwindData |  |
| 350 | `LPSAFEARRAY_UserSize64` | `0x4AAD0` | 897 | UnwindData |  |
| 288 | `VARIANT_UserMarshal` | `0x4AE60` | 995 | UnwindData |  |
| 359 | `VARIANT_UserMarshal64` | `0x4B250` | 1,022 | UnwindData |  |
| 263 | `VarUI2FromCy` | `0x4B660` | 47 | UnwindData |  |
| 134 | `VarUI1FromCy` | `0x4B6A0` | 70 | UnwindData |  |
| 52 | `VarI2FromCy` | `0x4B6F0` | 66 | UnwindData |  |
| 250 | `VarI1FromCy` | `0x4B740` | 70 | UnwindData |  |
| 62 | `VarI4FromCy` | `0x4B790` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `VarCyFromStr` | `0x4C190` | 154 | UnwindData |  |
| 304 | `VarCyMulI4` | `0x4C610` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `VarI8FromCy` | `0x4C6E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `VarCyFromDec` | `0x4C830` | 896 | UnwindData |  |
| 32 | `CreateStdDispatch` | `0x4D160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `VarDecFromI8` | `0x4D1A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `VarUI1FromDec` | `0x4D1F0` | 162 | UnwindData |  |
| 269 | `VarUI2FromDec` | `0x4D2A0` | 163 | UnwindData |  |
| 441 | `VarUI8FromDec` | `0x4D350` | 172 | UnwindData |  |
| 256 | `VarI1FromDec` | `0x4D410` | 172 | UnwindData |  |
| 208 | `VarI2FromDec` | `0x4D4D0` | 173 | UnwindData |  |
| 345 | `VarI8FromDec` | `0x4D590` | 197 | UnwindData |  |
| 282 | `VarUI4FromDec` | `0x4D690` | 157 | UnwindData |  |
| 224 | `VarDateFromDec` | `0x4D760` | 141 | UnwindData |  |
| 196 | `VarDecFromCy` | `0x4D8D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `VarCyFromI8` | `0x4D950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `VarI1FromI2` | `0x4D990` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `VarUI2FromI1` | `0x4D9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `VarUI4FromI1` | `0x4DA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `VarUI8FromI1` | `0x4DA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `VarUI8FromI2` | `0x4DA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `VarI1FromI4` | `0x4DA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `VarI1FromI8` | `0x4DA90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `VarI2FromI8` | `0x4DAC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `VarI1FromUI2` | `0x4DAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `VarI1FromUI4` | `0x4DB10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `VarDateFromCy` | `0x4DB40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `VarDateFromBool` | `0x4DB80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `VarDateFromI2` | `0x4DB80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `VarR8FromBool` | `0x4DB80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `VarR8FromI2` | `0x4DB80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `VarBoolFromDec` | `0x4DBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `VarI1FromR8` | `0x4DC10` | 50 | UnwindData |  |
| 133 | `VarUI1FromR8` | `0x4DC50` | 50 | UnwindData |  |
| 261 | `VarUI2FromR8` | `0x4DC90` | 51 | UnwindData |  |
| 311 | `VarCyCmp` | `0x4DCD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `VarUI4FromCy` | `0x4DD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `VarUI8FromCy` | `0x4DD50` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CreateErrorInfo` | `0x4F2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `GetErrorInfo` | `0x4F2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `SetErrorInfo` | `0x4F2D0` | 19,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CreateTypeLib` | `0x53D80` | 170 | UnwindData |  |
| 186 | `UnRegisterTypeLib` | `0x543F0` | 141 | UnwindData |  |
| 443 | `UnRegisterTypeLibForUser` | `0x54490` | 173 | UnwindData |  |
| 504 | *Ordinal Only* | `0x58F30` | 44 | UnwindData |  |
| 442 | `RegisterTypeLibForUser` | `0x59040` | 132 | UnwindData |  |
| 502 | *Ordinal Only* | `0x5A450` | 385 | UnwindData |  |
| 326 | `GetVarConversionLocaleSetting` | `0x5A5E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `OaEnablePerUserTLibRegistration` | `0x5A610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `SetVarConversionLocaleSetting` | `0x5A630` | 167 | UnwindData |  |
| 171 | `ClearCustData` | `0x6ED80` | 142 | UnwindData |  |
| 168 | `VarAbs` | `0x71600` | 617 | UnwindData |  |
| 310 | `VarCyRound` | `0x71870` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `VarFix` | `0x71900` | 508 | UnwindData |  |
| 173 | `VarNeg` | `0x71B10` | 678 | UnwindData |  |
| 317 | `VarR8Round` | `0x71DC0` | 226 | UnwindData |  |
| 175 | `VarRound` | `0x71EB0` | 519 | UnwindData |  |
| 318 | `VarCat` | `0x72270` | 205 | UnwindData |  |
| 329 | `VarCyMulI8` | `0x72350` | 122 | UnwindData |  |
| 158 | `VarPow` | `0x723D0` | 360 | UnwindData |  |
| 315 | `VarR8Pow` | `0x72540` | 210 | UnwindData |  |
| 152 | `VarEqv` | `0x72620` | 42 | UnwindData |  |
| 153 | `VarIdiv` | `0x72650` | 488 | UnwindData |  |
| 154 | `VarImp` | `0x72840` | 253 | UnwindData |  |
| 167 | `VarXor` | `0x72950` | 356 | UnwindData |  |
| 298 | `VarDecCmpR8` | `0x72AC0` | 114 | UnwindData |  |
| 316 | `VarR4CmpR8` | `0x72B40` | 67 | UnwindData |  |
| 306 | `VarCyAbs` | `0x72B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `VarCyAdd` | `0x72BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `VarCyCmpR8` | `0x72BF0` | 95 | UnwindData |  |
| 307 | `VarCyFix` | `0x72C60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `VarCyInt` | `0x72CA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `VarCyMul` | `0x72D10` | 317 | UnwindData |  |
| 309 | `VarCyNeg` | `0x72E60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `VarCySub` | `0x72E90` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `VarDecAbs` | `0x73270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `VarDecAdd` | `0x732A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `VarDecNeg` | `0x732B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `VarDecSub` | `0x732E0` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `VarBoolFromDate` | `0x73970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `VarBoolFromDisp` | `0x73980` | 57 | UnwindData |  |
| 233 | `VarBoolFromI1` | `0x739C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `VarBoolFromUI1` | `0x739C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `VarBoolFromI2` | `0x739E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `VarBoolFromUI2` | `0x739E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `VarBoolFromI4` | `0x73A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `VarBoolFromUI4` | `0x73A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `VarBoolFromI8` | `0x73A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `VarBoolFromUI8` | `0x73A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `VarBoolFromR4` | `0x73A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `VarBoolFromR8` | `0x73A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `VarBstrFromDisp` | `0x73A80` | 57 | UnwindData |  |
| 105 | `VarCyFromDisp` | `0x73AC0` | 57 | UnwindData |  |
| 367 | `VarCyFromUI8` | `0x73B00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `VarDateFromDisp` | `0x73B30` | 59 | UnwindData |  |
| 221 | `VarDateFromI1` | `0x73B80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `VarDateFromI4` | `0x73BC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `VarDateFromI8` | `0x73C00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `VarDateFromR4` | `0x73C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `VarDateFromR8` | `0x73C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `VarDateFromUI2` | `0x73CA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `VarDateFromUI4` | `0x73CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `VarDateFromUI8` | `0x73D20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `VarI1FromBool` | `0x73D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `VarUI1FromBool` | `0x73D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `VarI1FromDate` | `0x73D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `VarI1FromDisp` | `0x73DA0` | 55 | UnwindData |  |
| 244 | `VarI1FromUI1` | `0x73DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `VarI2FromBool` | `0x73E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `VarUI2FromBool` | `0x73E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `VarI2FromDate` | `0x73E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `VarI2FromDisp` | `0x73E20` | 57 | UnwindData |  |
| 48 | `VarI2FromUI1` | `0x73E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `VarUI2FromUI1` | `0x73E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `VarI2FromUI2` | `0x73E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `VarI2FromUI8` | `0x73E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `VarI4FromBool` | `0x73EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `VarI4FromI2` | `0x73EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `VarUI4FromBool` | `0x73EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `VarI4FromDate` | `0x73EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `VarI4FromDisp` | `0x73ED0` | 55 | UnwindData |  |
| 58 | `VarI4FromUI1` | `0x73F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `VarUI4FromUI1` | `0x73F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `VarI4FromUI2` | `0x73F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `VarUI4FromUI2` | `0x73F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `VarI4FromUI4` | `0x73F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `VarI8FromBool` | `0x73F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `VarI8FromI2` | `0x73F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `VarUI8FromBool` | `0x73F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `VarI8FromDate` | `0x73F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `VarI8FromDisp` | `0x73F80` | 57 | UnwindData |  |
| 333 | `VarI8FromUI1` | `0x73FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `VarUI8FromUI1` | `0x73FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `VarI8FromUI2` | `0x73FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `VarUI8FromUI2` | `0x73FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `VarI8FromUI4` | `0x73FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `VarUI8FromUI4` | `0x73FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `VarI8FromUI8` | `0x73FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `VarR4FromBool` | `0x74020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `VarR4FromI2` | `0x74020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `VarR4FromDate` | `0x74040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `VarR4FromDisp` | `0x74050` | 59 | UnwindData |  |
| 70 | `VarR4FromI4` | `0x740A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `VarR4FromUI2` | `0x740C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `VarR4FromUI4` | `0x740E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `VarR4FromUI8` | `0x74100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `VarR8FromDate` | `0x74140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `VarR8FromDisp` | `0x74150` | 59 | UnwindData |  |
| 80 | `VarR8FromI4` | `0x741A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `VarR8FromI8` | `0x741C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `VarR8FromUI2` | `0x741E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `VarR8FromUI4` | `0x74200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `VarR8FromUI8` | `0x74220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `VarUI1FromDate` | `0x74260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `VarUI1FromDisp` | `0x74270` | 55 | UnwindData |  |
| 237 | `VarUI1FromI1` | `0x742B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `VarUI1FromI8` | `0x742D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `VarUI1FromUI8` | `0x742D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `VarUI2FromDate` | `0x742F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `VarUI2FromDisp` | `0x74300` | 57 | UnwindData |  |
| 258 | `VarUI2FromI2` | `0x74340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `VarUI2FromI8` | `0x74360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `VarUI2FromUI8` | `0x74360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `VarUI4FromDate` | `0x74380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `VarUI4FromDisp` | `0x74390` | 55 | UnwindData |  |
| 272 | `VarUI4FromI4` | `0x743D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `VarUI8FromDate` | `0x743F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `VarUI8FromDisp` | `0x74400` | 57 | UnwindData |  |
| 428 | `VarUI8FromI8` | `0x74440` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `CreateDispTypeInfo` | `0x74870` | 58 | UnwindData |  |
| 28 | `DispGetParam` | `0x748D0` | 123 | UnwindData |  |
| 320 | `DllRegisterServer` | `0x75060` | 839 | UnwindData |  |
| 321 | `DllUnregisterServer` | `0x753B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `VariantTimeToDosDateTime` | `0x753C0` | 180 | UnwindData |  |
| 35 | `GetActiveObject` | `0x75480` | 78 | UnwindData |  |
| 322 | `GetRecordInfoFromGuids` | `0x787E0` | 376 | UnwindData |  |
| 417 | `OleCreatePropertyFrame` | `0x78DF0` | 94 | UnwindData |  |
| 416 | `OleCreatePropertyFrameIndirect` | `0x78E60` | 50 | UnwindData |  |
| 415 | `OleIconToCursor` | `0x78EA0` | 76 | UnwindData |  |
| 422 | `OleLoadPictureFile` | `0x78F00` | 51 | UnwindData |  |
| 402 | `OleLoadPictureFileEx` | `0x78F40` | 126 | UnwindData |  |
| 424 | `OleLoadPicturePath` | `0x78FD0` | 114 | UnwindData |  |
| 423 | `OleSavePictureFile` | `0x79050` | 62 | UnwindData |  |
| 353 | `SafeArrayAddRef` | `0x79210` | 124 | UnwindData |  |
| 354 | `SafeArrayReleaseData` | `0x792A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `VarDecFromBool` | `0x792E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `VarDecFromDate` | `0x79310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `VarDecFromDisp` | `0x79320` | 68 | UnwindData |  |
| 127 | `VarFormatCurrency` | `0x7A650` | 282 | UnwindData |  |
| 97 | `VarFormatDateTime` | `0x7A770` | 129 | UnwindData |  |
| 117 | `VarFormatPercent` | `0x7A800` | 247 | UnwindData |  |
| 129 | `VarMonthName` | `0x7A900` | 195 | UnwindData |  |
| 128 | `VarWeekdayName` | `0x7A9D0` | 240 | UnwindData |  |
| 11 | `VariantCopyInd` | `0x9E700` | 661 | UnwindData |  |
| 10 | `VariantCopy` | `0x9E9A0` | 41 | UnwindData |  |
| 9 | `VariantClear` | `0x9EC80` | 581 | UnwindData |  |
| 8 | `VariantInit` | `0x9EED0` | 0 | Indeterminate |  |
