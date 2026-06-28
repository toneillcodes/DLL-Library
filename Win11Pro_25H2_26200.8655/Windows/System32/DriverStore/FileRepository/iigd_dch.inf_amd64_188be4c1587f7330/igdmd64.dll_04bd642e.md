# Binary Specification: igdmd64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdmd64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `04bd642edef4b98172d348ae877c0529080ea5c0da5494ee229337a6e6578fcd`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseMetricsDevice` | `0x61260` | 23 | UnwindData |  |
| 3 | `OpenAdapterGroup` | `0x61340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OpenMetricsDevice` | `0x61350` | 28 | UnwindData |  |
| 5 | `OpenMetricsDeviceFromFile` | `0x614B0` | 364 | UnwindData |  |
| 2 | `ClosePerformanceInterface` | `0x542970` | 70 | UnwindData |  |
| 6 | `OpenPerformanceInterface` | `0x542AD0` | 111 | UnwindData |  |
