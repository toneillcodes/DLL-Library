# Binary Specification: rdpnanoTransport.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rdpnanoTransport.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8d698d07b309d57ff6a6bebd8ec96795cc6673382f6931a9bfcb4a8bee09d9e1`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllMain` | `0x86C0` | 2,078,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateRdpUdpStreamWrapper` | `0x203DD0` | 120 | UnwindData |  |
| 3 | `FreeRdpUdpStreamWrapper` | `0x204960` | 62 | UnwindData |  |
| 2 | `CreateRdpWebSocketStreamWrapper` | `0x20C6C0` | 115 | UnwindData |  |
| 4 | `FreeRdpWebSocketStreamWrapper` | `0x20C740` | 50 | UnwindData |  |
| 6 | `RdpNanoInitialize2` | `0x2115E0` | 166 | UnwindData |  |
