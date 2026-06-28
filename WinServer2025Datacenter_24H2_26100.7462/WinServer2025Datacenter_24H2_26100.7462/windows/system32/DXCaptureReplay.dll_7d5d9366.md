# Binary Specification: DXCaptureReplay.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DXCaptureReplay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7d5d9366d01b2a2731cb7bfa50d9648171756c575058cb35198728625cbed734`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `CreatePMCommsPUGA` | `0x46AE0` | 682 | UnwindData |  |
| 55 | `LazyAttachToInProc` | `0x571E0` | 48 | UnwindData |  |
| 56 | `LazyAttachToMonitor` | `0x57220` | 307 | UnwindData |  |
| 57 | `ReleaseCaptureSessionContext` | `0x57360` | 210 | UnwindData |  |
| 26 | `CheckForWindowClosure` | `0xB47C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CreateUtilityWindow` | `0xB47D0` | 191,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `GetReflectionLayer` | `0xE3500` | 354 | UnwindData |  |
| 1 | `CreateDXGIFactory1Generated` | `0x10D910` | 135 | UnwindData |  |
| 2 | `CreateDXGIFactory2Generated` | `0x10D9A0` | 149 | UnwindData |  |
| 3 | `CreateDXGIFactoryGenerated` | `0x10DA40` | 135 | UnwindData |  |
| 4 | `CustomEventGenerated` | `0x10DAD0` | 94 | UnwindData |  |
| 5 | `D2D1CreateDeviceContextGenerated` | `0x10DB40` | 152 | UnwindData |  |
| 6 | `D2D1CreateDeviceGenerated` | `0x10DBE0` | 152 | UnwindData |  |
| 7 | `D2D1CreateFactoryGenerated` | `0x10DC80` | 174 | UnwindData |  |
| 8 | `D3D10CreateDevice1Generated` | `0x10DD40` | 241 | UnwindData |  |
| 9 | `D3D10CreateDeviceAndSwapChain1Generated` | `0x10DE40` | 293 | UnwindData |  |
| 10 | `D3D10CreateDeviceAndSwapChainGenerated` | `0x10DF70` | 271 | UnwindData |  |
| 11 | `D3D10CreateDeviceGenerated` | `0x10E090` | 219 | UnwindData |  |
| 12 | `D3D11CreateDeviceAndSwapChainGenerated` | `0x10E180` | 369 | UnwindData |  |
| 13 | `D3D11CreateDeviceGenerated` | `0x10E300` | 311 | UnwindData |  |
| 14 | `D3D11On12CreateDeviceGenerated` | `0x10E440` | 311 | UnwindData |  |
| 15 | `D3D12CreateDeviceGenerated` | `0x10E580` | 172 | UnwindData |  |
| 16 | `D3D12EnableExperimentalFeaturesGenerated` | `0x10E640` | 174 | UnwindData |  |
| 17 | `D3D12FenceEventCompletionGenerated` | `0x10E700` | 129 | UnwindData |  |
| 18 | `D3D12GetDebugInterfaceGenerated` | `0x10E790` | 135 | UnwindData |  |
| 19 | `D3DCreateCaptureRecreationHelperGenerated` | `0x10E820` | 113 | UnwindData |  |
| 20 | `D3DPERF_BeginEventGenerated` | `0x10E8A0` | 167 | UnwindData |  |
| 21 | `D3DPERF_EndEventGenerated` | `0x10E950` | 135 | UnwindData |  |
| 22 | `D3DPERF_SetMarkerGenerated` | `0x10E9E0` | 164 | UnwindData |  |
| 23 | `D3DPERF_SetRegionGenerated` | `0x10EA90` | 164 | UnwindData |  |
| 24 | `DImageLoadGraphFromStringGenerated` | `0x10EB40` | 152 | UnwindData |  |
| 25 | `DXGIGetDebugInterface1Generated` | `0x10EBE0` | 149 | UnwindData |  |
| 29 | `GetRealPtrPtrCreateDXGIFactory` | `0x10EC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `GetRealPtrPtrCreateDXGIFactory1` | `0x10EC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `GetRealPtrPtrCreateDXGIFactory2` | `0x10ECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetRealPtrPtrCustomEvent` | `0x10ECB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `GetRealPtrPtrD2D1CreateDevice` | `0x10ECC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetRealPtrPtrD2D1CreateDeviceContext` | `0x10ECD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetRealPtrPtrD2D1CreateFactory` | `0x10ECE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `GetRealPtrPtrD3D10CreateDevice` | `0x10ECF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GetRealPtrPtrD3D10CreateDevice1` | `0x10ED00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `GetRealPtrPtrD3D10CreateDeviceAndSwapChain` | `0x10ED10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `GetRealPtrPtrD3D10CreateDeviceAndSwapChain1` | `0x10ED20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `GetRealPtrPtrD3D11CreateDevice` | `0x10ED30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `GetRealPtrPtrD3D11CreateDeviceAndSwapChain` | `0x10ED40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `GetRealPtrPtrD3D11On12CreateDevice` | `0x10ED50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetRealPtrPtrD3D12CreateDevice` | `0x10ED60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `GetRealPtrPtrD3D12EnableExperimentalFeatures` | `0x10ED70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `GetRealPtrPtrD3D12FenceEventCompletion` | `0x10ED80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `GetRealPtrPtrD3D12GetDebugInterface` | `0x10ED90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `GetRealPtrPtrD3DCreateCaptureRecreationHelper` | `0x10EDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `GetRealPtrPtrD3DPERF_BeginEvent` | `0x10EDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetRealPtrPtrD3DPERF_EndEvent` | `0x10EDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetRealPtrPtrD3DPERF_SetMarker` | `0x10EDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetRealPtrPtrD3DPERF_SetRegion` | `0x10EDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `GetRealPtrPtrDImageLoadGraphFromString` | `0x10EDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `GetRealPtrPtrDXGIGetDebugInterface1` | `0x10EE00` | 11,974,460 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
