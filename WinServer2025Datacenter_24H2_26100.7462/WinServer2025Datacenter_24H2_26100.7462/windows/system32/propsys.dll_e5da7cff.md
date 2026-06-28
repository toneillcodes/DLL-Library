# Binary Specification: propsys.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\propsys.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e5da7cff79f44d2c9fb6f56a3681c308c535b1a992571adf7d65e68e74e1aa9b`
* **Total Exported Functions:** 268

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 441 | *Ordinal Only* | `0x3F20` | 339 | UnwindData |  |
| 440 | *Ordinal Only* | `0x4E60` | 341 | UnwindData |  |
| 424 | *Ordinal Only* | `0x5100` | 62 | UnwindData |  |
| 68 | `PSGetPropertyKeyFromName` | `0x63E0` | 275 | UnwindData |  |
| 423 | *Ordinal Only* | `0x7280` | 408 | UnwindData |  |
| 62 | `PSGetNameFromPropertyKey` | `0x7420` | 202 | UnwindData |  |
| 46 | `PSCoerceToCanonicalValue` | `0x74F0` | 206 | UnwindData |  |
| 65 | `PSGetPropertyDescriptionByName` | `0x7CA0` | 256 | UnwindData |  |
| 64 | `PSGetPropertyDescription` | `0x9090` | 296 | UnwindData |  |
| 436 | `WinRTPropertyValueToPropVariant` | `0xF960` | 3,018 | UnwindData |  |
| 421 | *Ordinal Only* | `0x10680` | 527 | UnwindData |  |
| 192 | `VariantToFileTime` | `0x108C0` | 211 | UnwindData |  |
| 164 | `PropVariantToUInt64` | `0x109A0` | 251 | UnwindData |  |
| 420 | *Ordinal Only* | `0x10AB0` | 301 | UnwindData |  |
| 134 | `PropVariantToFileTime` | `0x10BF0` | 652 | UnwindData |  |
| 422 | *Ordinal Only* | `0x12020` | 194 | UnwindData |  |
| 167 | `PropVariantToUInt64WithDefault` | `0x120F0` | 59 | UnwindData |  |
| 33 | `InitVariantFromFileTime` | `0x121D0` | 159 | UnwindData |  |
| 444 | *Ordinal Only* | `0x15D20` | 749 | UnwindData |  |
| 81 | `PSPropertyBag_ReadPropertyKey` | `0x16230` | 228 | UnwindData |  |
| 76 | `PSPropertyBag_ReadGUID` | `0x16320` | 335 | UnwindData |  |
| 85 | `PSPropertyBag_ReadStrAlloc` | `0x16600` | 92 | UnwindData |  |
| 89 | `PSPropertyBag_ReadUnknown` | `0x16670` | 239 | UnwindData |  |
| 74 | `PSPropertyBag_ReadBSTR` | `0x16770` | 200 | UnwindData |  |
| 73 | `PSPropertyBag_ReadBOOL` | `0x16840` | 216 | UnwindData |  |
| 75 | `PSPropertyBag_ReadDWORD` | `0x16920` | 194 | UnwindData |  |
| 168 | `PropVariantToVariant` | `0x16DE0` | 873 | UnwindData |  |
| 67 | `PSGetPropertyFromPropertyStorage` | `0x17150` | 1,742 | UnwindData |  |
| 410 | *Ordinal Only* | `0x17150` | 1,742 | UnwindData |  |
| 63 | `PSGetNamedPropertyFromPropertyStorage` | `0x17D80` | 72 | UnwindData |  |
| 409 | *Ordinal Only* | `0x17D80` | 72 | UnwindData |  |
| 169 | `StgDeserializePropVariant` | `0x1A5F0` | 676 | UnwindData |  |
| 115 | `PropVariantGetElementCount` | `0x1A8A0` | 348 | UnwindData |  |
| 434 | *Ordinal Only* | `0x1AA10` | 151 | UnwindData |  |
| 111 | `PropVariantChangeType` | `0x1BB10` | 928 | UnwindData |  |
| 112 | `PropVariantCompareEx` | `0x1E870` | 104 | UnwindData |  |
| 12 | `InitPropVariantFromBuffer` | `0x22680` | 153 | UnwindData |  |
| 49 | `PSCreateMemoryPropertyStore` | `0x22790` | 58 | UnwindData |  |
| 407 | *Ordinal Only* | `0x22A40` | 205 | UnwindData |  |
| 24 | `InitPropVariantFromStringAsVector` | `0x22B20` | 61 | UnwindData |  |
| 152 | `PropVariantToStringAlloc` | `0x237C0` | 658 | UnwindData |  |
| 21 | `InitPropVariantFromPropVariantVectorElem` | `0x23E10` | 995 | UnwindData |  |
| 151 | `PropVariantToString` | `0x242A0` | 472 | UnwindData |  |
| 209 | `VariantToStringAlloc` | `0x24A50` | 259 | UnwindData |  |
| 45 | `InitVariantFromVariantArrayElem` | `0x24B60` | 436 | UnwindData |  |
| 174 | `VariantGetElementCount` | `0x24E00` | 127 | UnwindData |  |
| 125 | `PropVariantToBoolean` | `0x24F90` | 217 | UnwindData |  |
| 206 | `VariantToPropVariant` | `0x25A20` | 210 | UnwindData |  |
| 208 | `VariantToString` | `0x25F00` | 377 | UnwindData |  |
| 221 | `VariantToUInt64` | `0x26080` | 273 | UnwindData |  |
| 201 | `VariantToInt32WithDefault` | `0x26510` | 57 | UnwindData |  |
| 198 | `VariantToInt32` | `0x26550` | 263 | UnwindData |  |
| 217 | `VariantToUInt32` | `0x26660` | 231 | UnwindData |  |
| 220 | `VariantToUInt32WithDefault` | `0x26890` | 57 | UnwindData |  |
| 142 | `PropVariantToInt32` | `0x268D0` | 233 | UnwindData |  |
| 128 | `PropVariantToBooleanWithDefault` | `0x269C0` | 57 | UnwindData |  |
| 417 | *Ordinal Only* | `0x272C0` | 3,386 | UnwindData |  |
| 400 | *Ordinal Only* | `0x28470` | 189 | UnwindData |  |
| 50 | `PSCreateMultiplexPropertyStore` | `0x292B0` | 1,305 | UnwindData |  |
| 48 | `PSCreateDelayedMultiplexPropertyStore` | `0x299E0` | 217 | UnwindData |  |
| 408 | *Ordinal Only* | `0x29B80` | 175 | UnwindData |  |
| 51 | `PSCreatePropertyChangeArray` | `0x29CE0` | 50 | UnwindData |  |
| 47 | `PSCreateAdapterFromPropertyStore` | `0x2A2F0` | 187 | UnwindData |  |
| 53 | `PSCreatePropertyStoreFromPropertySetStorage` | `0x2A3C0` | 274 | UnwindData |  |
| 57 | `PSFormatForDisplayAlloc` | `0x2A4E0` | 148 | UnwindData |  |
| 66 | `PSGetPropertyDescriptionListFromString` | `0x2A580` | 227 | UnwindData |  |
| 69 | `PSGetPropertySystem` | `0x2A670` | 164 | UnwindData |  |
| 52 | `PSCreatePropertyStoreFromObject` | `0x2AAD0` | 53 | UnwindData |  |
| 56 | `PSFormatForDisplay` | `0x2ADC0` | 58 | UnwindData |  |
| 418 | *Ordinal Only* | `0x2C870` | 464 | UnwindData |  |
| 430 | *Ordinal Only* | `0x2C870` | 464 | UnwindData |  |
| 155 | `PropVariantToStringWithDefault` | `0x2CD80` | 7,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `PropVariantToStringVectorAlloc` | `0x2EBA0` | 787 | UnwindData |  |
| 84 | `PSPropertyBag_ReadStr` | `0x30780` | 152 | UnwindData |  |
| 87 | `PSPropertyBag_ReadType` | `0x30820` | 420 | UnwindData |  |
| 86 | `PSPropertyBag_ReadStream` | `0x31180` | 155 | UnwindData |  |
| 77 | `PSPropertyBag_ReadInt` | `0x318A0` | 103 | UnwindData |  |
| 78 | `PSPropertyBag_ReadLONG` | `0x318A0` | 103 | UnwindData |  |
| 160 | `PropVariantToUInt32` | `0x342A0` | 220 | UnwindData |  |
| 446 | *Ordinal Only* | `0x34390` | 584 | UnwindData |  |
| 25 | `InitPropVariantFromStringVector` | `0x345E0` | 573 | UnwindData |  |
| 212 | `VariantToStringWithDefault` | `0x3F410` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | *Ordinal Only* | `0x3F810` | 123 | UnwindData |  |
| 171 | `VariantCompare` | `0x3FFE0` | 1,859 | UnwindData |  |
| 163 | `PropVariantToUInt32WithDefault` | `0x45CE0` | 261 | UnwindData |  |
| 435 | `PropVariantToWinRTPropertyValue` | `0x489F0` | 4,691 | UnwindData |  |
| 145 | `PropVariantToInt32WithDefault` | `0x4BDF0` | 283 | UnwindData |  |
| 193 | `VariantToGUID` | `0x4C7F0` | 158 | UnwindData |  |
| 186 | `VariantToBuffer` | `0x4C8A0` | 304 | UnwindData |  |
| 137 | `PropVariantToGUID` | `0x4EF50` | 364 | UnwindData |  |
| 31 | `InitVariantFromBuffer` | `0x4F730` | 138 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x50B50` | 222 | UnwindData |  |
| 15 | `InitPropVariantFromFileTime` | `0x53030` | 3,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `PSPropertyBag_WriteStr` | `0x53E00` | 193 | UnwindData |  |
| 13 | `InitPropVariantFromCLSID` | `0x53F30` | 114 | UnwindData |  |
| 109 | `PSStringFromPropertyKey` | `0x556F0` | 154 | UnwindData |  |
| 91 | `PSPropertyBag_WriteBSTR` | `0x56CF0` | 100 | UnwindData |  |
| 44 | `InitVariantFromUInt64Array` | `0x57450` | 38 | UnwindData |  |
| 43 | `InitVariantFromUInt32Array` | `0x57480` | 38 | UnwindData |  |
| 37 | `InitVariantFromInt32Array` | `0x574B0` | 38 | UnwindData |  |
| 32 | `InitVariantFromDoubleArray` | `0x574E0` | 38 | UnwindData |  |
| 445 | *Ordinal Only* | `0x589A0` | 179 | UnwindData |  |
| 432 | *Ordinal Only* | `0x58D70` | 286 | UnwindData |  |
| 105 | `PSPropertyKeyFromString` | `0x58F50` | 192 | UnwindData |  |
| 129 | `PropVariantToBuffer` | `0x59600` | 165 | UnwindData |  |
| 439 | *Ordinal Only* | `0x59A50` | 173 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x5A2A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | *Ordinal Only* | `0x5A360` | 286 | UnwindData |  |
| 98 | `PSPropertyBag_WritePropertyKey` | `0x5A910` | 163 | UnwindData |  |
| 93 | `PSPropertyBag_WriteGUID` | `0x5A9C0` | 149 | UnwindData |  |
| 35 | `InitVariantFromGUIDAsString` | `0x5AA60` | 142 | UnwindData |  |
| 92 | `PSPropertyBag_WriteDWORD` | `0x5AB00` | 100 | UnwindData |  |
| 90 | `PSPropertyBag_WriteBOOL` | `0x5AEB0` | 118 | UnwindData |  |
| 185 | `VariantToBooleanWithDefault` | `0x5AF30` | 55 | UnwindData |  |
| 182 | `VariantToBoolean` | `0x5AF70` | 225 | UnwindData |  |
| 416 | *Ordinal Only* | `0x5C850` | 5,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PropVariantToBSTR` | `0x5DF40` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `PSPropertyBag_WriteStream` | `0x5E030` | 105 | UnwindData |  |
| 104 | `PSPropertyBag_WriteUnknown` | `0x5E030` | 105 | UnwindData |  |
| 406 | *Ordinal Only* | `0x5E620` | 274 | UnwindData |  |
| 156 | `PropVariantToUInt16` | `0x61FC0` | 213 | UnwindData |  |
| 79 | `PSPropertyBag_ReadPOINTL` | `0x62C80` | 436 | UnwindData |  |
| 82 | `PSPropertyBag_ReadRECTL` | `0x62E40` | 526 | UnwindData |  |
| 170 | `StgSerializePropVariant` | `0x63080` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `PropVariantToDouble` | `0x63870` | 227 | UnwindData |  |
| 17 | `InitPropVariantFromGUIDAsString` | `0x655A0` | 109 | UnwindData |  |
| 122 | `PropVariantGetUInt32Elem` | `0x65700` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `PSPropertyBag_WriteInt` | `0x65B30` | 100 | UnwindData |  |
| 22 | `InitPropVariantFromResource` | `0x660E0` | 125 | UnwindData |  |
| 72 | `PSPropertyBag_Delete` | `0x667B0` | 85 | UnwindData |  |
| 95 | `PSPropertyBag_WriteLONG` | `0x66A20` | 102 | UnwindData |  |
| 161 | `PropVariantToUInt32Vector` | `0x66A90` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PropVariantGetStringElem` | `0x674A0` | 411 | UnwindData |  |
| 55 | `PSEnumeratePropertyDescriptions` | `0x67AD0` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | *Ordinal Only* | `0x682C0` | 4,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `PropVariantToInt64` | `0x69520` | 256 | UnwindData |  |
| 19 | `InitPropVariantFromInt32Vector` | `0x69640` | 3,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PSPropertyBag_WritePOINTL` | `0x6A390` | 280 | UnwindData |  |
| 27 | `InitPropVariantFromUInt32Vector` | `0x6AB90` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `VariantToInt32Array` | `0x6AD70` | 14,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `PropVariantToUInt64Vector` | `0x6E5F0` | 51,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0x7B030` | 131 | UnwindData |  |
| 60 | `PSGetItemPropertyHandler` | `0x7C580` | 26 | UnwindData |  |
| 61 | `PSGetItemPropertyHandlerWithCreateObject` | `0x7C5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `PSLookupPropertyHandlerCLSID` | `0x7C5B0` | 56 | UnwindData |  |
| 433 | *Ordinal Only* | `0x7F8C0` | 224 | UnwindData |  |
| 438 | *Ordinal Only* | `0x7F9B0` | 5,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | *Ordinal Only* | `0x80DF0` | 187 | UnwindData |  |
| 405 | *Ordinal Only* | `0x81580` | 281 | UnwindData |  |
| 54 | `PSCreateSimplePropertyChange` | `0x816A0` | 38 | UnwindData |  |
| 447 | *Ordinal Only* | `0x816D0` | 159 | UnwindData |  |
| 80 | `PSPropertyBag_ReadPOINTS` | `0x81780` | 73 | UnwindData |  |
| 83 | `PSPropertyBag_ReadSHORT` | `0x817D0` | 105 | UnwindData |  |
| 88 | `PSPropertyBag_ReadULONGLONG` | `0x81840` | 105 | UnwindData |  |
| 97 | `PSPropertyBag_WritePOINTS` | `0x818B0` | 57 | UnwindData |  |
| 99 | `PSPropertyBag_WriteRECTL` | `0x818F0` | 441 | UnwindData |  |
| 100 | `PSPropertyBag_WriteSHORT` | `0x81AB0` | 101 | UnwindData |  |
| 103 | `PSPropertyBag_WriteULONGLONG` | `0x81B20` | 100 | UnwindData |  |
| 58 | `PSFormatPropertyValue` | `0x84210` | 141 | UnwindData |  |
| 59 | `PSGetImageReferenceForValue` | `0x842B0` | 131 | UnwindData |  |
| 70 | `PSGetPropertyValue` | `0x84340` | 128 | UnwindData |  |
| 106 | `PSRefreshPropertySchema` | `0x843D0` | 108 | UnwindData |  |
| 107 | `PSRegisterPropertySchema` | `0x84450` | 123 | UnwindData |  |
| 108 | `PSSetPropertyValue` | `0x844E0` | 120 | UnwindData |  |
| 110 | `PSUnregisterPropertySchema` | `0x84560` | 123 | UnwindData |  |
| 425 | *Ordinal Only* | `0x86620` | 296 | UnwindData |  |
| 426 | *Ordinal Only* | `0x86750` | 170 | UnwindData |  |
| 443 | *Ordinal Only* | `0x87330` | 239 | UnwindData |  |
| 442 | *Ordinal Only* | `0x87430` | 322 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x88BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllUnregisterServer` | `0x88BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | *Ordinal Only* | `0x88C20` | 33 | UnwindData |  |
| 3 | `GetProxyDllInfo` | `0x88C50` | 26,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ClearPropVariantArray` | `0x8F220` | 56 | UnwindData |  |
| 11 | `InitPropVariantFromBooleanVector` | `0x8F260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | *Ordinal Only* | `0x8F270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `InitPropVariantFromDoubleVector` | `0x8F280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `InitPropVariantFromFileTimeVector` | `0x8F290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `InitPropVariantFromInt16Vector` | `0x8F2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `InitPropVariantFromInt64Vector` | `0x8F2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `InitPropVariantFromStrRet` | `0x8F2C0` | 56 | UnwindData |  |
| 411 | *Ordinal Only* | `0x8F300` | 271 | UnwindData |  |
| 26 | `InitPropVariantFromUInt16Vector` | `0x8F420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `InitPropVariantFromUInt64Vector` | `0x8F430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `InitPropVariantVectorFromPropVariant` | `0x8F440` | 363 | UnwindData |  |
| 113 | `PropVariantGetBooleanElem` | `0x8F5F0` | 90 | UnwindData |  |
| 114 | `PropVariantGetDoubleElem` | `0x8F650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `PropVariantGetFileTimeElem` | `0x8F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PropVariantGetInt16Elem` | `0x8F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `PropVariantGetInt32Elem` | `0x8F6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PropVariantGetInt64Elem` | `0x8F6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `PropVariantGetUInt16Elem` | `0x8F6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PropVariantGetUInt64Elem` | `0x8F710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PropVariantToBooleanVector` | `0x8F730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PropVariantToBooleanVectorAlloc` | `0x8F740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PropVariantToDoubleVector` | `0x8F750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `PropVariantToDoubleVectorAlloc` | `0x8F760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `PropVariantToDoubleWithDefault` | `0x8F770` | 65 | UnwindData |  |
| 135 | `PropVariantToFileTimeVector` | `0x8F7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `PropVariantToFileTimeVectorAlloc` | `0x8F7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `PropVariantToInt16` | `0x8F7E0` | 201 | UnwindData |  |
| 139 | `PropVariantToInt16Vector` | `0x8F8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `PropVariantToInt16VectorAlloc` | `0x8F8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `PropVariantToInt16WithDefault` | `0x8F8D0` | 59 | UnwindData |  |
| 143 | `PropVariantToInt32Vector` | `0x8F920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `PropVariantToInt32VectorAlloc` | `0x8F930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `PropVariantToInt64Vector` | `0x8F940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `PropVariantToInt64VectorAlloc` | `0x8F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `PropVariantToInt64WithDefault` | `0x8F960` | 59 | UnwindData |  |
| 150 | `PropVariantToStrRet` | `0x8F9B0` | 234 | UnwindData |  |
| 412 | *Ordinal Only* | `0x8FAA0` | 154 | UnwindData |  |
| 153 | `PropVariantToStringVector` | `0x8FB40` | 484 | UnwindData |  |
| 404 | *Ordinal Only* | `0x8FD30` | 287 | UnwindData |  |
| 157 | `PropVariantToUInt16Vector` | `0x8FE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `PropVariantToUInt16VectorAlloc` | `0x8FE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `PropVariantToUInt16WithDefault` | `0x8FE80` | 59 | UnwindData |  |
| 162 | `PropVariantToUInt32VectorAlloc` | `0x8FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `PropVariantToUInt64VectorAlloc` | `0x8FEE0` | 31,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | *Ordinal Only* | `0x97A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | *Ordinal Only* | `0x97AA0` | 111 | UnwindData |  |
| 403 | *Ordinal Only* | `0x99040` | 342 | UnwindData |  |
| 6 | `ClearVariantArray` | `0x99820` | 56 | UnwindData |  |
| 30 | `InitVariantFromBooleanArray` | `0x99860` | 38 | UnwindData |  |
| 34 | `InitVariantFromFileTimeArray` | `0x99890` | 240 | UnwindData |  |
| 36 | `InitVariantFromInt16Array` | `0x99990` | 41 | UnwindData |  |
| 38 | `InitVariantFromInt64Array` | `0x999C0` | 38 | UnwindData |  |
| 39 | `InitVariantFromResource` | `0x999F0` | 151 | UnwindData |  |
| 40 | `InitVariantFromStrRet` | `0x99A90` | 110 | UnwindData |  |
| 41 | `InitVariantFromStringArray` | `0x99B10` | 243 | UnwindData |  |
| 42 | `InitVariantFromUInt16Array` | `0x99C10` | 38 | UnwindData |  |
| 172 | `VariantGetBooleanElem` | `0x99C40` | 90 | UnwindData |  |
| 173 | `VariantGetDoubleElem` | `0x99CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `VariantGetInt16Elem` | `0x99CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `VariantGetInt32Elem` | `0x99CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `VariantGetInt64Elem` | `0x99D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `VariantGetStringElem` | `0x99D20` | 309 | UnwindData |  |
| 179 | `VariantGetUInt16Elem` | `0x99E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `VariantGetUInt32Elem` | `0x99E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `VariantGetUInt64Elem` | `0x99EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `VariantToBooleanArray` | `0x99EC0` | 81 | UnwindData |  |
| 184 | `VariantToBooleanArrayAlloc` | `0x99F20` | 81 | UnwindData |  |
| 187 | `VariantToDosDateTime` | `0x99F80` | 327 | UnwindData |  |
| 188 | `VariantToDouble` | `0x9A0D0` | 235 | UnwindData |  |
| 189 | `VariantToDoubleArray` | `0x9A1D0` | 81 | UnwindData |  |
| 190 | `VariantToDoubleArrayAlloc` | `0x9A230` | 81 | UnwindData |  |
| 191 | `VariantToDoubleWithDefault` | `0x9A290` | 65 | UnwindData |  |
| 194 | `VariantToInt16` | `0x9A2E0` | 214 | UnwindData |  |
| 195 | `VariantToInt16Array` | `0x9A3C0` | 81 | UnwindData |  |
| 196 | `VariantToInt16ArrayAlloc` | `0x9A420` | 81 | UnwindData |  |
| 197 | `VariantToInt16WithDefault` | `0x9A480` | 59 | UnwindData |  |
| 200 | `VariantToInt32ArrayAlloc` | `0x9A4D0` | 81 | UnwindData |  |
| 202 | `VariantToInt64` | `0x9A530` | 269 | UnwindData |  |
| 203 | `VariantToInt64Array` | `0x9A650` | 81 | UnwindData |  |
| 204 | `VariantToInt64ArrayAlloc` | `0x9A6B0` | 81 | UnwindData |  |
| 205 | `VariantToInt64WithDefault` | `0x9A710` | 59 | UnwindData |  |
| 207 | `VariantToStrRet` | `0x9A760` | 65 | UnwindData |  |
| 210 | `VariantToStringArray` | `0x9A7B0` | 373 | UnwindData |  |
| 211 | `VariantToStringArrayAlloc` | `0x9A930` | 407 | UnwindData |  |
| 213 | `VariantToUInt16` | `0x9AAD0` | 219 | UnwindData |  |
| 214 | `VariantToUInt16Array` | `0x9ABC0` | 81 | UnwindData |  |
| 215 | `VariantToUInt16ArrayAlloc` | `0x9AC20` | 81 | UnwindData |  |
| 216 | `VariantToUInt16WithDefault` | `0x9AC80` | 59 | UnwindData |  |
| 218 | `VariantToUInt32Array` | `0x9ACD0` | 81 | UnwindData |  |
| 219 | `VariantToUInt32ArrayAlloc` | `0x9AD30` | 81 | UnwindData |  |
| 222 | `VariantToUInt64Array` | `0x9AD90` | 81 | UnwindData |  |
| 223 | `VariantToUInt64ArrayAlloc` | `0x9ADF0` | 81 | UnwindData |  |
| 224 | `VariantToUInt64WithDefault` | `0x9AE50` | 59 | UnwindData |  |
| 4 | `SHGetPropertyStoreForWindow` | `0xA19B0` | 156 | UnwindData |  |
