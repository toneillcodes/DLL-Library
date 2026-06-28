# Binary Specification: aadauthhelper.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\aadauthhelper.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c96c8986f015580353d83c2bb180f5dc453c9d440be9956cfb6d2cadecbe93d9`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseFidoAuthenticationSession` | `0x48E0` | 89 | UnwindData |  |
| 2 | `CreateAuthBuffer` | `0x4940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateResourceAccountAuthBuffer` | `0x4950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateTokenAuthBuffer` | `0x4960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CreateTokenAuthBufferEx` | `0x4980` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetFidoAuthenticationSessionStatus` | `0x4B00` | 144 | UnwindData |  |
| 7 | `GetSerializedAuthBuffer` | `0x4BA0` | 129 | UnwindData |  |
| 8 | `StartChangingFidoPin` | `0x4DB0` | 121 | UnwindData |  |
| 9 | `StartFidoAuthenticationSession` | `0x4E30` | 138 | UnwindData |  |
| 10 | `StartSigningFidoClientData` | `0x4EC0` | 107 | UnwindData |  |
