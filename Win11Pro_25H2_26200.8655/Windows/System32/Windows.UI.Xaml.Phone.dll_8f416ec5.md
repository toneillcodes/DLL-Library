# Binary Specification: Windows.UI.Xaml.Phone.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.UI.Xaml.Phone.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8f416ec53f4d7fc34c14e67d2137ca66058939a7fb664cf75c2c2fe787f0bf46`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8D90` | 81 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x8DF0` | 465 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x8FD0` | 231 | UnwindData |  |
| 5 | `GetDependencyLocatorStorage` | `0x9350` | 47 | UnwindData |  |
| 14 | `XamlTestHookFreePhoneResourceLibrary` | `0x93A0` | 42 | UnwindData |  |
| 10 | `XamlControlsGetPlatformMetadataProvider` | `0xF3D0` | 69,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SendTelemetryOnSuspend` | `0x203D0` | 21,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateApplicationBarProxy` | `0x259B0` | 175 | UnwindData |  |
| 7 | `XamlControlsCalculateFlyoutPlacement` | `0x25EA0` | 846 | UnwindData |  |
| 8 | `XamlControlsGetDatePickerSelection` | `0x29E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `XamlControlsGetListPickerSelection` | `0x29E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `XamlControlsGetTimePickerSelection` | `0x29E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `XamlControlsTestHookCreateLoopingSelector` | `0x29E70` | 50 | UnwindData |  |
| 11 | `XamlControlsGetPlatformResourcesModuleHandle` | `0x29EB0` | 827,802 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
