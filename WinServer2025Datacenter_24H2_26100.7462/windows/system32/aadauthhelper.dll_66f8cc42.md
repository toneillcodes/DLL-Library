# Binary Specification: aadauthhelper.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\aadauthhelper.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `66f8cc42001a6c972339eef3dac2980def298bec866496fc258d5291ceb8bf24`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseFidoAuthenticationSession` | `0x48D0` | 89 | UnwindData |  |
| 2 | `CreateAuthBuffer` | `0x4930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateResourceAccountAuthBuffer` | `0x4940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateTokenAuthBuffer` | `0x4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CreateTokenAuthBufferEx` | `0x4970` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetFidoAuthenticationSessionStatus` | `0x4AF0` | 144 | UnwindData |  |
| 7 | `GetSerializedAuthBuffer` | `0x4B90` | 129 | UnwindData |  |
| 8 | `StartChangingFidoPin` | `0x4DA0` | 121 | UnwindData |  |
| 9 | `StartFidoAuthenticationSession` | `0x4E20` | 138 | UnwindData |  |
| 10 | `StartSigningFidoClientData` | `0x4EB0` | 107 | UnwindData |  |
