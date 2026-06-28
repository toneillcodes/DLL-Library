# Binary Specification: htui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\htui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b0d685b38a87c4ddda543cf98b3f29bf5672187e1f956c61f1e1d3587db3d4e4`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x1A40` | 129 | UnwindData |  |
| 2 | `HTUI_ColorAdjustment` | `0x1AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `HTUI_ColorAdjustmentA` | `0x1AE0` | 360 | UnwindData |  |
| 4 | `HTUI_ColorAdjustmentW` | `0x1C50` | 330 | UnwindData |  |
| 5 | `HTUI_DeviceColorAdjustment` | `0x1DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `HTUI_DeviceColorAdjustmentA` | `0x1DB0` | 177 | UnwindData |  |
| 7 | `HTUI_DeviceColorAdjustmentW` | `0x1E70` | 387 | UnwindData |  |
