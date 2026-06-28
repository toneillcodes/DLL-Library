# Binary Specification: dssec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dssec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `66be6c5c96f0391291fa870233fb247f3e44f18c98c522c848782e6435a35f93`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x1E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x1E30` | 204 | UnwindData |  |
| 1 | `DSCreateISecurityInfoObject` | `0x51A0` | 73 | UnwindData |  |
| 4 | `DSCreateISecurityInfoObjectEx` | `0x51F0` | 350 | UnwindData |  |
| 2 | `DSCreateSecurityPage` | `0x5360` | 152 | UnwindData |  |
| 3 | `DSEditSecurity` | `0x5400` | 409 | UnwindData |  |
