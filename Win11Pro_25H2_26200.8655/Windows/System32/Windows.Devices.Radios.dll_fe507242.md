# Binary Specification: Windows.Devices.Radios.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Devices.Radios.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe507242f22060f86c3bcef4c34473dfe46fd8421b01d2086f4e4447eb0ba900`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x16F00` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x16F40` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x16F80` | 134 | UnwindData |  |
| 4 | `DllMain` | `0x17010` | 223 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x17100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x17130` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RadioDeviceCreate` | `0x17820` | 249 | UnwindData |  |
| 8 | `RadioDeviceDelete` | `0x17920` | 238 | UnwindData |  |
| 9 | `RadioDeviceStart` | `0x17A20` | 206 | UnwindData |  |
| 10 | `RadioDeviceStop` | `0x17B00` | 191 | UnwindData |  |
| 11 | `StartRadioMonitor` | `0x190F0` | 181 | UnwindData |  |
| 12 | `StopRadioMonitor` | `0x191B0` | 113 | UnwindData |  |
