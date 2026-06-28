# Binary Specification: wdigest.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wdigest.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9e0635e324218c7502442430b74dd1b072c5e04b0547f3076dc95da3010d21b7`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllMain` | `0xB0E0` | 120 | UnwindData |  |
| 4 | `CredentialUpdateFree` | `0x15B20` | 20 | UnwindData |  |
| 2 | `CredentialUpdateRegister` | `0x25CD0` | 31 | UnwindData |  |
| 5 | `CredentialUpdateNotify` | `0x25D00` | 1,708 | UnwindData |  |
| 1 | `SpInitialize` | `0x27A20` | 1,391 | UnwindData |  |
| 7 | `SpLsaModeInitialize` | `0x27FA0` | 670 | UnwindData |  |
| 3 | `SsiCredentialsUpdateNotify` | `0x287C0` | 1,653 | UnwindData |  |
| 9 | `SsiCredentialsUpdateFree` | `0x2AC80` | 183 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x32BA0` | 404 | UnwindData |  |
| 8 | `SpUserModeInitialize` | `0x33C20` | 394 | UnwindData |  |
