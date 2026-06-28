# Binary Specification: wdigest.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wdigest.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b7a68c43b065df2df1e82705f559f74df093b989271258b37d729c4f97edb168`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllMain` | `0xB1C0` | 120 | UnwindData |  |
| 4 | `CredentialUpdateFree` | `0x15BA0` | 20 | UnwindData |  |
| 2 | `CredentialUpdateRegister` | `0x26080` | 31 | UnwindData |  |
| 5 | `CredentialUpdateNotify` | `0x260B0` | 1,708 | UnwindData |  |
| 1 | `SpInitialize` | `0x27DD0` | 1,391 | UnwindData |  |
| 7 | `SpLsaModeInitialize` | `0x28350` | 670 | UnwindData |  |
| 3 | `SsiCredentialsUpdateNotify` | `0x28B70` | 1,653 | UnwindData |  |
| 9 | `SsiCredentialsUpdateFree` | `0x2B030` | 183 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x32F50` | 404 | UnwindData |  |
| 8 | `SpUserModeInitialize` | `0x33FD0` | 394 | UnwindData |  |
