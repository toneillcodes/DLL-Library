# Binary Specification: EdgeManager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\EdgeManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c7aa911e4ae9bc8aad2274ac3d648620af408a7c6f3cbef651b2813a12660323`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `GetWebDriverHostInstance` | `0x1BC0` | 316 | UnwindData |  |
| 19 | `EnsureServiceWorkerEnvironmentForWebView` | `0x6C00` | 60 | UnwindData |  |
| 7 | `CreateCoreWebViewControl` | `0xA6A0` | 164 | UnwindData |  |
| 20 | `GetProxyDllInfo` | `0xEE30` | 28,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllCanUnloadNow` | `0x15E90` | 94 | UnwindData |  |
| 14 | `DllGetActivationFactory` | `0x15F00` | 45 | UnwindData |  |
| 15 | `DllGetClassObject` | `0x15F40` | 133 | UnwindData |  |
| 16 | `DllInstall` | `0x15FD0` | 274 | UnwindData |  |
| 17 | `DllRegisterServer` | `0x160F0` | 91 | UnwindData |  |
| 18 | `DllUnregisterServer` | `0x16160` | 85 | UnwindData |  |
| 6 | `CreateCoreWebViewComponentAndUninitializedCoreWebViewComponentCallbackForWebInstance` | `0x18590` | 667 | UnwindData |  |
| 8 | `CreateCoreWebViewHostProcess` | `0x18840` | 162 | UnwindData |  |
| 9 | `CreateCoreWebViewOOP` | `0x188F0` | 653 | UnwindData |  |
| 10 | `CreateWebViewControlAcceleratorKeyPressedEventArgs` | `0x18B90` | 258 | UnwindData |  |
| 11 | `CreateWebViewControlAndInitializeCoreWebViewComponentCallback` | `0x18CA0` | 732 | UnwindData |  |
| 12 | `CreateWebViewControlMoveFocusRequestedEventArgs` | `0x18F90` | 378 | UnwindData |  |
| 5 | `EnsureWebDriverForWebViewHost` | `0x3D4B0` | 99 | UnwindData |  |
| 1 | `CreateEdgeIsoSession` | `0x62240` | 16,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateWebRuntimeDebugTargetClient` | `0x661C0` | 229 | UnwindData |  |
| 4 | `CreateWebRuntimeDiagnosticsTarget` | `0x662B0` | 243 | UnwindData |  |
| 3 | `CreateWebRuntimeDebugTargetManager` | `0x6AD20` | 127 | UnwindData |  |
