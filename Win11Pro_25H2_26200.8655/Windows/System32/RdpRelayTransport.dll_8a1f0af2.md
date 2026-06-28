# Binary Specification: RdpRelayTransport.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\RdpRelayTransport.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8a1f0af21a90d387c55ba667c65ea9858b6e41782db8aae9116e4af4aebe9e01`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA2E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA310` | 281 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xA710` | 283 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xA840` | 142 | UnwindData |  |
| 5 | `RDPAPI_CreateInstance` | `0xA8E0` | 175,100 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
