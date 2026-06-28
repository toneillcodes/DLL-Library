# Binary Specification: Windows.Devices.Radios.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Devices.Radios.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eea85f659867b2504f2daf053ce3f08ca1f2a28a3f4c2d569abdd8cda435ae4c`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x16E50` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x16E90` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x16ED0` | 134 | UnwindData |  |
| 4 | `DllMain` | `0x16F60` | 223 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x17050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x17080` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RadioDeviceCreate` | `0x17770` | 249 | UnwindData |  |
| 8 | `RadioDeviceDelete` | `0x17870` | 238 | UnwindData |  |
| 9 | `RadioDeviceStart` | `0x17970` | 206 | UnwindData |  |
| 10 | `RadioDeviceStop` | `0x17A50` | 191 | UnwindData |  |
| 11 | `StartRadioMonitor` | `0x19040` | 181 | UnwindData |  |
| 12 | `StopRadioMonitor` | `0x19100` | 113 | UnwindData |  |
