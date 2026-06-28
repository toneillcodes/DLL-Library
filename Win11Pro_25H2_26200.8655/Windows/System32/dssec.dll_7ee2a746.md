# Binary Specification: dssec.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dssec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7ee2a746562ca4fdf3ef541634f2d916cbf24358ec2a0afdd55c7cbf6b1fb7ac`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x2BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x2BC0` | 204 | UnwindData |  |
| 1 | `DSCreateISecurityInfoObject` | `0x5F30` | 73 | UnwindData |  |
| 4 | `DSCreateISecurityInfoObjectEx` | `0x5F80` | 350 | UnwindData |  |
| 2 | `DSCreateSecurityPage` | `0x60F0` | 152 | UnwindData |  |
| 3 | `DSEditSecurity` | `0x6190` | 409 | UnwindData |  |
