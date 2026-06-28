# Binary Specification: dxgi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dxgi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93263bbef4f481aece8cb9183a66728bb0be7198d9f7e0c7eea5204d65b6e40f`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ApplyCompatResolutionQuirking` | `0x1B7C0` | 642 | UnwindData |  |
| 20 | `DXGIReportAdapterConfiguration` | `0x1CF40` | 48 | UnwindData |  |
| 3 | `CompatValue` | `0x246A0` | 201 | UnwindData |  |
| 2 | `CompatString` | `0x24840` | 824 | UnwindData |  |
| 17 | `DXGIDeclareAdapterRemovalSupport` | `0x341E0` | 112 | UnwindData |  |
| 10 | `CreateDXGIFactory` | `0x4BF90` | 99 | UnwindData |  |
| 11 | `CreateDXGIFactory1` | `0x4C0C0` | 99 | UnwindData |  |
| 12 | `CreateDXGIFactory2` | `0x50640` | 77 | UnwindData |  |
| 18 | `DXGIDisableVBlankVirtualization` | `0x5CC40` | 143 | UnwindData |  |
| 13 | `DXGID3D10CreateDevice` | `0x5F700` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DXGID3D10CreateLayeredDevice` | `0x5F700` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DXGID3D10RegisterLayers` | `0x5F700` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DXGID3D10GetLayeredDeviceSize` | `0x600E0` | 36,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PIXBeginCapture` | `0x600E0` | 36,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PIXEndCapture` | `0x600E0` | 36,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PIXGetCaptureState` | `0x600E0` | 36,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SetAppCompatStringPointer` | `0x69160` | 101,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DXGIDumpJournal` | `0x81C90` | 117 | UnwindData |  |
| 9 | `UpdateHMDEmulationStatus` | `0x897B0` | 98 | UnwindData |  |
| 19 | `DXGIGetDebugInterface1` | `0x8C0A0` | 77 | UnwindData |  |
