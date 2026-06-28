# Binary Specification: propsys.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\propsys.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a3f82327191b5c4a8645c934aa8d958ad0e767ff9ea40d1de15898cf399ef791`
* **Total Exported Functions:** 268

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 441 | *Ordinal Only* | `0x3F60` | 339 | UnwindData |  |
| 440 | *Ordinal Only* | `0x4EA0` | 341 | UnwindData |  |
| 424 | *Ordinal Only* | `0x5140` | 62 | UnwindData |  |
| 68 | `PSGetPropertyKeyFromName` | `0x6420` | 275 | UnwindData |  |
| 423 | *Ordinal Only* | `0x72C0` | 408 | UnwindData |  |
| 62 | `PSGetNameFromPropertyKey` | `0x7460` | 202 | UnwindData |  |
| 46 | `PSCoerceToCanonicalValue` | `0x7530` | 206 | UnwindData |  |
| 65 | `PSGetPropertyDescriptionByName` | `0x7CE0` | 256 | UnwindData |  |
| 64 | `PSGetPropertyDescription` | `0x90D0` | 296 | UnwindData |  |
| 436 | `WinRTPropertyValueToPropVariant` | `0xF9A0` | 3,018 | UnwindData |  |
| 421 | *Ordinal Only* | `0x106C0` | 527 | UnwindData |  |
| 192 | `VariantToFileTime` | `0x10900` | 211 | UnwindData |  |
| 164 | `PropVariantToUInt64` | `0x109E0` | 251 | UnwindData |  |
| 420 | *Ordinal Only* | `0x10AF0` | 301 | UnwindData |  |
| 134 | `PropVariantToFileTime` | `0x10C30` | 652 | UnwindData |  |
| 422 | *Ordinal Only* | `0x12060` | 194 | UnwindData |  |
| 167 | `PropVariantToUInt64WithDefault` | `0x12130` | 59 | UnwindData |  |
| 33 | `InitVariantFromFileTime` | `0x12210` | 159 | UnwindData |  |
| 444 | *Ordinal Only* | `0x15D70` | 749 | UnwindData |  |
| 81 | `PSPropertyBag_ReadPropertyKey` | `0x16280` | 228 | UnwindData |  |
| 76 | `PSPropertyBag_ReadGUID` | `0x16370` | 335 | UnwindData |  |
| 85 | `PSPropertyBag_ReadStrAlloc` | `0x16650` | 92 | UnwindData |  |
| 89 | `PSPropertyBag_ReadUnknown` | `0x166C0` | 239 | UnwindData |  |
| 74 | `PSPropertyBag_ReadBSTR` | `0x167C0` | 200 | UnwindData |  |
| 73 | `PSPropertyBag_ReadBOOL` | `0x16890` | 216 | UnwindData |  |
| 75 | `PSPropertyBag_ReadDWORD` | `0x16970` | 194 | UnwindData |  |
| 168 | `PropVariantToVariant` | `0x16E30` | 873 | UnwindData |  |
| 67 | `PSGetPropertyFromPropertyStorage` | `0x171A0` | 1,742 | UnwindData |  |
| 410 | *Ordinal Only* | `0x171A0` | 1,742 | UnwindData |  |
| 63 | `PSGetNamedPropertyFromPropertyStorage` | `0x17DD0` | 72 | UnwindData |  |
| 409 | *Ordinal Only* | `0x17DD0` | 72 | UnwindData |  |
| 169 | `StgDeserializePropVariant` | `0x1A640` | 676 | UnwindData |  |
| 115 | `PropVariantGetElementCount` | `0x1A8F0` | 348 | UnwindData |  |
| 434 | *Ordinal Only* | `0x1AA60` | 151 | UnwindData |  |
| 111 | `PropVariantChangeType` | `0x1BB60` | 928 | UnwindData |  |
| 112 | `PropVariantCompareEx` | `0x1E8C0` | 104 | UnwindData |  |
| 12 | `InitPropVariantFromBuffer` | `0x226D0` | 153 | UnwindData |  |
| 49 | `PSCreateMemoryPropertyStore` | `0x227E0` | 58 | UnwindData |  |
| 407 | *Ordinal Only* | `0x22A90` | 205 | UnwindData |  |
| 24 | `InitPropVariantFromStringAsVector` | `0x22B70` | 61 | UnwindData |  |
| 152 | `PropVariantToStringAlloc` | `0x23810` | 658 | UnwindData |  |
| 21 | `InitPropVariantFromPropVariantVectorElem` | `0x23E60` | 995 | UnwindData |  |
| 151 | `PropVariantToString` | `0x242F0` | 472 | UnwindData |  |
| 209 | `VariantToStringAlloc` | `0x24AA0` | 259 | UnwindData |  |
| 45 | `InitVariantFromVariantArrayElem` | `0x24BB0` | 436 | UnwindData |  |
| 174 | `VariantGetElementCount` | `0x24E50` | 127 | UnwindData |  |
| 125 | `PropVariantToBoolean` | `0x24FE0` | 217 | UnwindData |  |
| 206 | `VariantToPropVariant` | `0x25A70` | 210 | UnwindData |  |
| 208 | `VariantToString` | `0x25F50` | 377 | UnwindData |  |
| 221 | `VariantToUInt64` | `0x260D0` | 273 | UnwindData |  |
| 201 | `VariantToInt32WithDefault` | `0x26560` | 57 | UnwindData |  |
| 198 | `VariantToInt32` | `0x265A0` | 263 | UnwindData |  |
| 217 | `VariantToUInt32` | `0x266B0` | 231 | UnwindData |  |
| 220 | `VariantToUInt32WithDefault` | `0x268E0` | 57 | UnwindData |  |
| 142 | `PropVariantToInt32` | `0x26920` | 233 | UnwindData |  |
| 128 | `PropVariantToBooleanWithDefault` | `0x26A10` | 57 | UnwindData |  |
| 417 | *Ordinal Only* | `0x27310` | 3,386 | UnwindData |  |
| 400 | *Ordinal Only* | `0x284C0` | 189 | UnwindData |  |
| 50 | `PSCreateMultiplexPropertyStore` | `0x29300` | 1,305 | UnwindData |  |
| 48 | `PSCreateDelayedMultiplexPropertyStore` | `0x29A30` | 217 | UnwindData |  |
| 408 | *Ordinal Only* | `0x29BD0` | 175 | UnwindData |  |
| 51 | `PSCreatePropertyChangeArray` | `0x29D30` | 50 | UnwindData |  |
| 47 | `PSCreateAdapterFromPropertyStore` | `0x2A340` | 187 | UnwindData |  |
| 53 | `PSCreatePropertyStoreFromPropertySetStorage` | `0x2A410` | 274 | UnwindData |  |
| 57 | `PSFormatForDisplayAlloc` | `0x2A530` | 148 | UnwindData |  |
| 66 | `PSGetPropertyDescriptionListFromString` | `0x2A5D0` | 227 | UnwindData |  |
| 69 | `PSGetPropertySystem` | `0x2A6C0` | 164 | UnwindData |  |
| 52 | `PSCreatePropertyStoreFromObject` | `0x2AB20` | 53 | UnwindData |  |
| 56 | `PSFormatForDisplay` | `0x2AE10` | 58 | UnwindData |  |
| 418 | *Ordinal Only* | `0x2C8C0` | 464 | UnwindData |  |
| 430 | *Ordinal Only* | `0x2C8C0` | 464 | UnwindData |  |
| 155 | `PropVariantToStringWithDefault` | `0x2CDD0` | 7,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `PropVariantToStringVectorAlloc` | `0x2EBF0` | 787 | UnwindData |  |
| 84 | `PSPropertyBag_ReadStr` | `0x307D0` | 152 | UnwindData |  |
| 87 | `PSPropertyBag_ReadType` | `0x30870` | 420 | UnwindData |  |
| 86 | `PSPropertyBag_ReadStream` | `0x311D0` | 155 | UnwindData |  |
| 77 | `PSPropertyBag_ReadInt` | `0x318F0` | 103 | UnwindData |  |
| 78 | `PSPropertyBag_ReadLONG` | `0x318F0` | 103 | UnwindData |  |
| 160 | `PropVariantToUInt32` | `0x342F0` | 220 | UnwindData |  |
| 446 | *Ordinal Only* | `0x343E0` | 584 | UnwindData |  |
| 25 | `InitPropVariantFromStringVector` | `0x34630` | 573 | UnwindData |  |
| 212 | `VariantToStringWithDefault` | `0x3F460` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | *Ordinal Only* | `0x3F860` | 123 | UnwindData |  |
| 171 | `VariantCompare` | `0x40030` | 1,859 | UnwindData |  |
| 163 | `PropVariantToUInt32WithDefault` | `0x45D30` | 261 | UnwindData |  |
| 435 | `PropVariantToWinRTPropertyValue` | `0x48A40` | 4,691 | UnwindData |  |
| 145 | `PropVariantToInt32WithDefault` | `0x4BE40` | 283 | UnwindData |  |
| 193 | `VariantToGUID` | `0x4C840` | 158 | UnwindData |  |
| 186 | `VariantToBuffer` | `0x4C8F0` | 304 | UnwindData |  |
| 137 | `PropVariantToGUID` | `0x4E8B0` | 364 | UnwindData |  |
| 31 | `InitVariantFromBuffer` | `0x4F090` | 138 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x504B0` | 222 | UnwindData |  |
| 15 | `InitPropVariantFromFileTime` | `0x52990` | 3,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `PSPropertyBag_WriteStr` | `0x53760` | 193 | UnwindData |  |
| 13 | `InitPropVariantFromCLSID` | `0x53890` | 114 | UnwindData |  |
| 109 | `PSStringFromPropertyKey` | `0x55050` | 154 | UnwindData |  |
| 91 | `PSPropertyBag_WriteBSTR` | `0x56650` | 100 | UnwindData |  |
| 44 | `InitVariantFromUInt64Array` | `0x56DB0` | 38 | UnwindData |  |
| 43 | `InitVariantFromUInt32Array` | `0x56DE0` | 38 | UnwindData |  |
| 37 | `InitVariantFromInt32Array` | `0x56E10` | 38 | UnwindData |  |
| 32 | `InitVariantFromDoubleArray` | `0x56E40` | 38 | UnwindData |  |
| 445 | *Ordinal Only* | `0x58200` | 179 | UnwindData |  |
| 432 | *Ordinal Only* | `0x585D0` | 286 | UnwindData |  |
| 105 | `PSPropertyKeyFromString` | `0x587B0` | 192 | UnwindData |  |
| 129 | `PropVariantToBuffer` | `0x58E60` | 165 | UnwindData |  |
| 439 | *Ordinal Only* | `0x592B0` | 173 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x59B00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | *Ordinal Only* | `0x59BC0` | 286 | UnwindData |  |
| 98 | `PSPropertyBag_WritePropertyKey` | `0x5A170` | 163 | UnwindData |  |
| 93 | `PSPropertyBag_WriteGUID` | `0x5A220` | 149 | UnwindData |  |
| 35 | `InitVariantFromGUIDAsString` | `0x5A2C0` | 142 | UnwindData |  |
| 92 | `PSPropertyBag_WriteDWORD` | `0x5A360` | 100 | UnwindData |  |
| 90 | `PSPropertyBag_WriteBOOL` | `0x5A620` | 118 | UnwindData |  |
| 185 | `VariantToBooleanWithDefault` | `0x5A6A0` | 55 | UnwindData |  |
| 182 | `VariantToBoolean` | `0x5A6E0` | 225 | UnwindData |  |
| 416 | *Ordinal Only* | `0x5BFC0` | 7,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PropVariantToBSTR` | `0x5DB80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `PSPropertyBag_WriteStream` | `0x5DC70` | 105 | UnwindData |  |
| 104 | `PSPropertyBag_WriteUnknown` | `0x5DC70` | 105 | UnwindData |  |
| 406 | *Ordinal Only* | `0x5E3E0` | 274 | UnwindData |  |
| 156 | `PropVariantToUInt16` | `0x61DB0` | 213 | UnwindData |  |
| 79 | `PSPropertyBag_ReadPOINTL` | `0x62A70` | 436 | UnwindData |  |
| 82 | `PSPropertyBag_ReadRECTL` | `0x62C30` | 526 | UnwindData |  |
| 170 | `StgSerializePropVariant` | `0x62E70` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `PropVariantToDouble` | `0x63660` | 227 | UnwindData |  |
| 17 | `InitPropVariantFromGUIDAsString` | `0x65390` | 109 | UnwindData |  |
| 122 | `PropVariantGetUInt32Elem` | `0x654F0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `PSPropertyBag_WriteInt` | `0x65930` | 100 | UnwindData |  |
| 22 | `InitPropVariantFromResource` | `0x65EE0` | 125 | UnwindData |  |
| 72 | `PSPropertyBag_Delete` | `0x665B0` | 85 | UnwindData |  |
| 95 | `PSPropertyBag_WriteLONG` | `0x66820` | 102 | UnwindData |  |
| 161 | `PropVariantToUInt32Vector` | `0x66890` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PropVariantGetStringElem` | `0x672F0` | 411 | UnwindData |  |
| 55 | `PSEnumeratePropertyDescriptions` | `0x678C0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | *Ordinal Only* | `0x68140` | 4,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `PropVariantToInt64` | `0x693A0` | 256 | UnwindData |  |
| 19 | `InitPropVariantFromInt32Vector` | `0x694C0` | 3,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PSPropertyBag_WritePOINTL` | `0x6A210` | 280 | UnwindData |  |
| 27 | `InitPropVariantFromUInt32Vector` | `0x6AA10` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `VariantToInt32Array` | `0x6ABF0` | 14,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `PropVariantToUInt64Vector` | `0x6E5A0` | 52,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0x7B110` | 131 | UnwindData |  |
| 60 | `PSGetItemPropertyHandler` | `0x7C660` | 26 | UnwindData |  |
| 61 | `PSGetItemPropertyHandlerWithCreateObject` | `0x7C680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `PSLookupPropertyHandlerCLSID` | `0x7C690` | 56 | UnwindData |  |
| 433 | *Ordinal Only* | `0x7F9A0` | 224 | UnwindData |  |
| 438 | *Ordinal Only* | `0x7FA90` | 5,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | *Ordinal Only* | `0x80ED0` | 187 | UnwindData |  |
| 405 | *Ordinal Only* | `0x81660` | 281 | UnwindData |  |
| 54 | `PSCreateSimplePropertyChange` | `0x81780` | 38 | UnwindData |  |
| 447 | *Ordinal Only* | `0x817B0` | 159 | UnwindData |  |
| 80 | `PSPropertyBag_ReadPOINTS` | `0x81860` | 73 | UnwindData |  |
| 83 | `PSPropertyBag_ReadSHORT` | `0x818B0` | 105 | UnwindData |  |
| 88 | `PSPropertyBag_ReadULONGLONG` | `0x81920` | 105 | UnwindData |  |
| 97 | `PSPropertyBag_WritePOINTS` | `0x81990` | 57 | UnwindData |  |
| 99 | `PSPropertyBag_WriteRECTL` | `0x819D0` | 441 | UnwindData |  |
| 100 | `PSPropertyBag_WriteSHORT` | `0x81B90` | 101 | UnwindData |  |
| 103 | `PSPropertyBag_WriteULONGLONG` | `0x81C00` | 100 | UnwindData |  |
| 58 | `PSFormatPropertyValue` | `0x842F0` | 141 | UnwindData |  |
| 59 | `PSGetImageReferenceForValue` | `0x84390` | 131 | UnwindData |  |
| 70 | `PSGetPropertyValue` | `0x84420` | 128 | UnwindData |  |
| 106 | `PSRefreshPropertySchema` | `0x844B0` | 108 | UnwindData |  |
| 107 | `PSRegisterPropertySchema` | `0x84530` | 123 | UnwindData |  |
| 108 | `PSSetPropertyValue` | `0x845C0` | 120 | UnwindData |  |
| 110 | `PSUnregisterPropertySchema` | `0x84640` | 123 | UnwindData |  |
| 425 | *Ordinal Only* | `0x86700` | 296 | UnwindData |  |
| 426 | *Ordinal Only* | `0x86830` | 170 | UnwindData |  |
| 443 | *Ordinal Only* | `0x87410` | 239 | UnwindData |  |
| 442 | *Ordinal Only* | `0x87510` | 322 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x88CA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllUnregisterServer` | `0x88CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | *Ordinal Only* | `0x88D00` | 33 | UnwindData |  |
| 3 | `GetProxyDllInfo` | `0x88D30` | 26,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ClearPropVariantArray` | `0x8F300` | 56 | UnwindData |  |
| 11 | `InitPropVariantFromBooleanVector` | `0x8F340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | *Ordinal Only* | `0x8F350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `InitPropVariantFromDoubleVector` | `0x8F360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `InitPropVariantFromFileTimeVector` | `0x8F370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `InitPropVariantFromInt16Vector` | `0x8F380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `InitPropVariantFromInt64Vector` | `0x8F390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `InitPropVariantFromStrRet` | `0x8F3A0` | 56 | UnwindData |  |
| 411 | *Ordinal Only* | `0x8F3E0` | 271 | UnwindData |  |
| 26 | `InitPropVariantFromUInt16Vector` | `0x8F500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `InitPropVariantFromUInt64Vector` | `0x8F510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `InitPropVariantVectorFromPropVariant` | `0x8F520` | 363 | UnwindData |  |
| 113 | `PropVariantGetBooleanElem` | `0x8F6D0` | 90 | UnwindData |  |
| 114 | `PropVariantGetDoubleElem` | `0x8F730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `PropVariantGetFileTimeElem` | `0x8F750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PropVariantGetInt16Elem` | `0x8F770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `PropVariantGetInt32Elem` | `0x8F790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PropVariantGetInt64Elem` | `0x8F7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `PropVariantGetUInt16Elem` | `0x8F7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PropVariantGetUInt64Elem` | `0x8F7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PropVariantToBooleanVector` | `0x8F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PropVariantToBooleanVectorAlloc` | `0x8F820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PropVariantToDoubleVector` | `0x8F830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `PropVariantToDoubleVectorAlloc` | `0x8F840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `PropVariantToDoubleWithDefault` | `0x8F850` | 65 | UnwindData |  |
| 135 | `PropVariantToFileTimeVector` | `0x8F8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `PropVariantToFileTimeVectorAlloc` | `0x8F8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `PropVariantToInt16` | `0x8F8C0` | 201 | UnwindData |  |
| 139 | `PropVariantToInt16Vector` | `0x8F990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `PropVariantToInt16VectorAlloc` | `0x8F9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `PropVariantToInt16WithDefault` | `0x8F9B0` | 59 | UnwindData |  |
| 143 | `PropVariantToInt32Vector` | `0x8FA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `PropVariantToInt32VectorAlloc` | `0x8FA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `PropVariantToInt64Vector` | `0x8FA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `PropVariantToInt64VectorAlloc` | `0x8FA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `PropVariantToInt64WithDefault` | `0x8FA40` | 59 | UnwindData |  |
| 150 | `PropVariantToStrRet` | `0x8FA90` | 234 | UnwindData |  |
| 412 | *Ordinal Only* | `0x8FB80` | 154 | UnwindData |  |
| 153 | `PropVariantToStringVector` | `0x8FC20` | 484 | UnwindData |  |
| 404 | *Ordinal Only* | `0x8FE10` | 287 | UnwindData |  |
| 157 | `PropVariantToUInt16Vector` | `0x8FF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `PropVariantToUInt16VectorAlloc` | `0x8FF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `PropVariantToUInt16WithDefault` | `0x8FF60` | 59 | UnwindData |  |
| 162 | `PropVariantToUInt32VectorAlloc` | `0x8FFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `PropVariantToUInt64VectorAlloc` | `0x8FFC0` | 31,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | *Ordinal Only* | `0x97B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | *Ordinal Only* | `0x97B90` | 111 | UnwindData |  |
| 403 | *Ordinal Only* | `0x99130` | 342 | UnwindData |  |
| 6 | `ClearVariantArray` | `0x99910` | 56 | UnwindData |  |
| 30 | `InitVariantFromBooleanArray` | `0x99950` | 38 | UnwindData |  |
| 34 | `InitVariantFromFileTimeArray` | `0x99980` | 240 | UnwindData |  |
| 36 | `InitVariantFromInt16Array` | `0x99A80` | 41 | UnwindData |  |
| 38 | `InitVariantFromInt64Array` | `0x99AB0` | 38 | UnwindData |  |
| 39 | `InitVariantFromResource` | `0x99AE0` | 151 | UnwindData |  |
| 40 | `InitVariantFromStrRet` | `0x99B80` | 110 | UnwindData |  |
| 41 | `InitVariantFromStringArray` | `0x99C00` | 243 | UnwindData |  |
| 42 | `InitVariantFromUInt16Array` | `0x99D00` | 38 | UnwindData |  |
| 172 | `VariantGetBooleanElem` | `0x99D30` | 90 | UnwindData |  |
| 173 | `VariantGetDoubleElem` | `0x99D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `VariantGetInt16Elem` | `0x99DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `VariantGetInt32Elem` | `0x99DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `VariantGetInt64Elem` | `0x99DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `VariantGetStringElem` | `0x99E10` | 309 | UnwindData |  |
| 179 | `VariantGetUInt16Elem` | `0x99F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `VariantGetUInt32Elem` | `0x99F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `VariantGetUInt64Elem` | `0x99F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `VariantToBooleanArray` | `0x99FB0` | 81 | UnwindData |  |
| 184 | `VariantToBooleanArrayAlloc` | `0x9A010` | 81 | UnwindData |  |
| 187 | `VariantToDosDateTime` | `0x9A070` | 327 | UnwindData |  |
| 188 | `VariantToDouble` | `0x9A1C0` | 235 | UnwindData |  |
| 189 | `VariantToDoubleArray` | `0x9A2C0` | 81 | UnwindData |  |
| 190 | `VariantToDoubleArrayAlloc` | `0x9A320` | 81 | UnwindData |  |
| 191 | `VariantToDoubleWithDefault` | `0x9A380` | 65 | UnwindData |  |
| 194 | `VariantToInt16` | `0x9A3D0` | 214 | UnwindData |  |
| 195 | `VariantToInt16Array` | `0x9A4B0` | 81 | UnwindData |  |
| 196 | `VariantToInt16ArrayAlloc` | `0x9A510` | 81 | UnwindData |  |
| 197 | `VariantToInt16WithDefault` | `0x9A570` | 59 | UnwindData |  |
| 200 | `VariantToInt32ArrayAlloc` | `0x9A5C0` | 81 | UnwindData |  |
| 202 | `VariantToInt64` | `0x9A620` | 269 | UnwindData |  |
| 203 | `VariantToInt64Array` | `0x9A740` | 81 | UnwindData |  |
| 204 | `VariantToInt64ArrayAlloc` | `0x9A7A0` | 81 | UnwindData |  |
| 205 | `VariantToInt64WithDefault` | `0x9A800` | 59 | UnwindData |  |
| 207 | `VariantToStrRet` | `0x9A850` | 65 | UnwindData |  |
| 210 | `VariantToStringArray` | `0x9A8A0` | 373 | UnwindData |  |
| 211 | `VariantToStringArrayAlloc` | `0x9AA20` | 407 | UnwindData |  |
| 213 | `VariantToUInt16` | `0x9ABC0` | 219 | UnwindData |  |
| 214 | `VariantToUInt16Array` | `0x9ACB0` | 81 | UnwindData |  |
| 215 | `VariantToUInt16ArrayAlloc` | `0x9AD10` | 81 | UnwindData |  |
| 216 | `VariantToUInt16WithDefault` | `0x9AD70` | 59 | UnwindData |  |
| 218 | `VariantToUInt32Array` | `0x9ADC0` | 81 | UnwindData |  |
| 219 | `VariantToUInt32ArrayAlloc` | `0x9AE20` | 81 | UnwindData |  |
| 222 | `VariantToUInt64Array` | `0x9AE80` | 81 | UnwindData |  |
| 223 | `VariantToUInt64ArrayAlloc` | `0x9AEE0` | 81 | UnwindData |  |
| 224 | `VariantToUInt64WithDefault` | `0x9AF40` | 59 | UnwindData |  |
| 4 | `SHGetPropertyStoreForWindow` | `0xA2A80` | 156 | UnwindData |  |
