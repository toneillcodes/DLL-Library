# Binary Specification: EdgeManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\EdgeManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f8109d5c62ba7b00b57e49d363330171dd62067cc071de65ce54fbeca4fefbfb`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `GetWebDriverHostInstance` | `0x1BC0` | 316 | UnwindData |  |
| 19 | `EnsureServiceWorkerEnvironmentForWebView` | `0x6DF0` | 60 | UnwindData |  |
| 7 | `CreateCoreWebViewControl` | `0xA690` | 164 | UnwindData |  |
| 20 | `GetProxyDllInfo` | `0xEE10` | 28,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllCanUnloadNow` | `0x15E70` | 94 | UnwindData |  |
| 14 | `DllGetActivationFactory` | `0x15EE0` | 45 | UnwindData |  |
| 15 | `DllGetClassObject` | `0x15F20` | 133 | UnwindData |  |
| 16 | `DllInstall` | `0x15FB0` | 274 | UnwindData |  |
| 17 | `DllRegisterServer` | `0x160D0` | 91 | UnwindData |  |
| 18 | `DllUnregisterServer` | `0x16140` | 85 | UnwindData |  |
| 6 | `CreateCoreWebViewComponentAndUninitializedCoreWebViewComponentCallbackForWebInstance` | `0x18570` | 667 | UnwindData |  |
| 8 | `CreateCoreWebViewHostProcess` | `0x18820` | 162 | UnwindData |  |
| 9 | `CreateCoreWebViewOOP` | `0x188D0` | 653 | UnwindData |  |
| 10 | `CreateWebViewControlAcceleratorKeyPressedEventArgs` | `0x18B70` | 258 | UnwindData |  |
| 11 | `CreateWebViewControlAndInitializeCoreWebViewComponentCallback` | `0x18C80` | 732 | UnwindData |  |
| 12 | `CreateWebViewControlMoveFocusRequestedEventArgs` | `0x18F70` | 378 | UnwindData |  |
| 5 | `EnsureWebDriverForWebViewHost` | `0x3D1A0` | 99 | UnwindData |  |
| 1 | `CreateEdgeIsoSession` | `0x61EB0` | 16,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateWebRuntimeDebugTargetClient` | `0x65E20` | 229 | UnwindData |  |
| 4 | `CreateWebRuntimeDiagnosticsTarget` | `0x65F10` | 243 | UnwindData |  |
| 3 | `CreateWebRuntimeDebugTargetManager` | `0x6A970` | 127 | UnwindData |  |
