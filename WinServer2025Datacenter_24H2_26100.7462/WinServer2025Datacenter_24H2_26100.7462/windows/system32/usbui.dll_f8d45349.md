# Binary Specification: usbui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usbui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f8d45349b5437c469ec3107ad375756bad56e06b86b45f2420683b5660874559`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CPlApplet` | `0x2B40` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `USBControllerBandwidthPage` | `0x2B40` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `USBHubPowerPage` | `0x2B40` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UsbControlPanelApplet` | `0x2B40` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x3120` | 174 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3260` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x3260` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `USBControllerPropPageProvider` | `0x3A00` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `USBDevicePropPageProvider` | `0x3BE0` | 186 | UnwindData |  |
| 9 | `USBErrorHandler` | `0x3CA0` | 635 | UnwindData |  |
| 11 | `USBHubPropPageProvider` | `0x3F30` | 611 | UnwindData |  |
