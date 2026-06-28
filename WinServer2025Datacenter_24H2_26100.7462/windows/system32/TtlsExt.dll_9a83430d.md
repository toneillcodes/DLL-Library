# Binary Specification: TtlsExt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TtlsExt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a83430d632dad8a7a00f1537fc1572ca35648f091b3190f136c10cc91f5d4a4`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `TtlsExt_GetConfigCacheOnlyCertValidation` | `0x4A90` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `TtlsExt_GetConfigForceNotDomainJoined` | `0x4A90` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `TtlsExt_ShowHelp` | `0x4A90` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `TtlsExt_InvokeServerAuthentication` | `0x7530` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllCanUnloadNow` | `0x7E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0x7E50` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllRegisterServer` | `0x7FC0` | 91 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0x8030` | 17 | UnwindData |  |
| 8 | `TtlsExt_FreeMemoryExt` | `0x8050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `TtlsExt_GetContextData` | `0x8070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `TtlsExt_GetUserCredentials` | `0x8080` | 1,091 | UnwindData |  |
| 1 | `TtlsExt_EapPeerInvokeConfigUI` | `0xD410` | 897 | UnwindData |  |
| 2 | `TtlsExt_InvokeNonEapMethodUI` | `0xE8C0` | 438 | UnwindData |  |
