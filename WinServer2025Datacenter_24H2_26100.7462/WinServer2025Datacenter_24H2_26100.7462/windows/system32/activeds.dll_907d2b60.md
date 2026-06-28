# Binary Specification: activeds.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\activeds.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `907d2b60cc59eff485d40cce41b372cf706a89ea5cd66fd2565314485a3de122`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `ADsDecodeBinaryData` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ADsDecodeBinaryData` |
| 20 | `ADsEncodeBinaryData` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ADsEncodeBinaryData` |
| 13 | `ADsGetLastError` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ADsGetLastError` |
| 12 | `ADsSetLastError` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ADsSetLastError` |
| 14 | `AllocADsMem` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.AllocADsMem` |
| 17 | `AllocADsStr` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.AllocADsStr` |
| 15 | `FreeADsMem` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.FreeADsMem` |
| 18 | `FreeADsStr` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.FreeADsStr` |
| 16 | `ReallocADsMem` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ReallocADsMem` |
| 19 | `ReallocADsStr` | `0x0` | - | Forwarded | Forwarded to: `ADSLDPC.ReallocADsStr` |
| 3 | `ADsGetObject` | `0x2910` | 55 | UnwindData |  |
| 9 | `ADsOpenObject` | `0x3300` | 103 | UnwindData |  |
| 25 | `AdsTypeToPropVariant2` | `0x3AD0` | 1,496 | UnwindData |  |
| 11 | `DllGetClassObject` | `0x4EE0` | 21 | UnwindData |  |
| 7 | `ADsBuildVarArrayStr` | `0x5C70` | 343 | UnwindData |  |
| 5 | `ADsFreeEnumerator` | `0x6210` | 36 | UnwindData |  |
| 4 | `ADsBuildEnumerator` | `0x6310` | 120 | UnwindData |  |
| 6 | `ADsEnumerateNext` | `0x6880` | 22 | UnwindData |  |
| 10 | `DllCanUnloadNow` | `0x6EC0` | 40 | UnwindData |  |
| 23 | `AdsFreeAdsValues` | `0x9BE0` | 49 | UnwindData |  |
| 22 | `AdsTypeToPropVariant` | `0x9C20` | 37 | UnwindData |  |
| 21 | `PropVariantToAdsType` | `0x9C50` | 39 | UnwindData |  |
| 26 | `PropVariantToAdsType2` | `0x9C80` | 504 | UnwindData |  |
| 8 | `ADsBuildVarArrayInt` | `0x230E0` | 267 | UnwindData |  |
| 29 | `BinarySDToSecurityDescriptor` | `0x23200` | 119 | UnwindData |  |
| 30 | `SecurityDescriptorToBinarySD` | `0x23280` | 224 | UnwindData |  |
| 27 | `ConvertSecDescriptorToVariant` | `0x29060` | 1,068 | UnwindData |  |
| 28 | `ConvertSecurityDescriptorToSecDes` | `0x2BF60` | 1,169 | UnwindData |  |
| 31 | `ConvertTrusteeToSid` | `0x2C400` | 1,749 | UnwindData |  |
