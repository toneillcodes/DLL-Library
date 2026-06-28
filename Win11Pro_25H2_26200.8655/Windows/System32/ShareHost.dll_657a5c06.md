# Binary Specification: ShareHost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ShareHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `657a5c06b993f54f7c56b304d610ed8ef361aa4ddd3a608988771aaf4b4b36e3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3A90` | 104 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x6A10` | 15,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetActivationFactory` | `0xA690` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xA6D0` | 111 | UnwindData |  |
| 5 | `ResolveConnectedSharePlatformToken` | `0x2A220` | 77 | UnwindData |  |
