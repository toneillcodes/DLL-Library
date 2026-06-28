# Binary Specification: Windows.Networking.Connectivity.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Networking.Connectivity.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd1f617e5b49f3b0615a66791ffdedccf6dfe8e4942c157c3e88146bba2d9466`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x39A0` | 196 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x3A70` | 205 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x30490` | 318 | UnwindData |  |
| 9 | `TeredoExtAcquireTeredoConsumerHandle` | `0x390A0` | 172 | UnwindData |  |
| 1 | `SetHostNameMediaStreamingMode` | `0x3A000` | 344 | UnwindData |  |
| 7 | `FixDisabledComponentsForTeredo` | `0x45FF0` | 139 | UnwindData |  |
| 8 | `RefreshTeredoClientState` | `0x46090` | 141 | UnwindData |  |
| 10 | `TeredoExtReleaseTeredoConsumerHandle` | `0x46130` | 159 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x46240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x46270` | 158,981 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
