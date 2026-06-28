# Binary Specification: Windows.UI.Xaml.Phone.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.UI.Xaml.Phone.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `42f5fd80d9b25be7df832d5a03d218fe155389c516dd3cc7dc45ba6777b18704`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8CA0` | 81 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x8D00` | 465 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x8EE0` | 231 | UnwindData |  |
| 5 | `GetDependencyLocatorStorage` | `0x9260` | 47 | UnwindData |  |
| 14 | `XamlTestHookFreePhoneResourceLibrary` | `0x92B0` | 42 | UnwindData |  |
| 10 | `XamlControlsGetPlatformMetadataProvider` | `0xF2E0` | 69,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SendTelemetryOnSuspend` | `0x202E0` | 21,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateApplicationBarProxy` | `0x258C0` | 175 | UnwindData |  |
| 7 | `XamlControlsCalculateFlyoutPlacement` | `0x25DB0` | 846 | UnwindData |  |
| 8 | `XamlControlsGetDatePickerSelection` | `0x29CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `XamlControlsGetListPickerSelection` | `0x29CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `XamlControlsGetTimePickerSelection` | `0x29D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `XamlControlsTestHookCreateLoopingSelector` | `0x29D10` | 50 | UnwindData |  |
| 11 | `XamlControlsGetPlatformResourcesModuleHandle` | `0x29D50` | 830,010 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
