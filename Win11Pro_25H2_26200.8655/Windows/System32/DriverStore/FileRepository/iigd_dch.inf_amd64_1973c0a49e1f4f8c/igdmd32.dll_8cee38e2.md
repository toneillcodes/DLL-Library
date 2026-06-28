# Binary Specification: igdmd32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdmd32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `8cee38e208e518e2a8f241646df4407c45e2a421a5a12ccd4003eb8aa828686b`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseMetricsDevice` | `0x23C70` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `OpenAdapterGroup` | `0x23D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OpenMetricsDevice` | `0x23D50` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `OpenMetricsDeviceFromFile` | `0x23E70` | 6,060,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ClosePerformanceInterface` | `0x5EB840` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `OpenPerformanceInterface` | `0x5EB970` | 399,320 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
