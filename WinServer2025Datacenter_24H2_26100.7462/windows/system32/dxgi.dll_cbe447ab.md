# Binary Specification: dxgi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dxgi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cbe447aba1b90fb104c089ab461356fb5453a63f888b4e707d3f72c2b80dc092`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CompatValue` | `0x9FC0` | 201 | UnwindData |  |
| 2 | `CompatString` | `0xABE0` | 460 | UnwindData |  |
| 17 | `DXGIDeclareAdapterRemovalSupport` | `0x25A70` | 112 | UnwindData |  |
| 1 | `ApplyCompatResolutionQuirking` | `0x2A990` | 642 | UnwindData |  |
| 20 | `DXGIReportAdapterConfiguration` | `0x2C110` | 48 | UnwindData |  |
| 10 | `CreateDXGIFactory` | `0x4DE50` | 99 | UnwindData |  |
| 11 | `CreateDXGIFactory1` | `0x4DF80` | 99 | UnwindData |  |
| 12 | `CreateDXGIFactory2` | `0x52BB0` | 77 | UnwindData |  |
| 18 | `DXGIDisableVBlankVirtualization` | `0x60A30` | 143 | UnwindData |  |
| 13 | `DXGID3D10CreateDevice` | `0x63770` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DXGID3D10CreateLayeredDevice` | `0x63770` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DXGID3D10RegisterLayers` | `0x63770` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DXGID3D10GetLayeredDeviceSize` | `0x64150` | 26,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PIXBeginCapture` | `0x64150` | 26,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PIXEndCapture` | `0x64150` | 26,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PIXGetCaptureState` | `0x64150` | 26,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SetAppCompatStringPointer` | `0x6A990` | 104,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DXGIDumpJournal` | `0x840A0` | 117 | UnwindData |  |
| 9 | `UpdateHMDEmulationStatus` | `0x8C0A0` | 98 | UnwindData |  |
| 19 | `DXGIGetDebugInterface1` | `0x8E940` | 77 | UnwindData |  |
