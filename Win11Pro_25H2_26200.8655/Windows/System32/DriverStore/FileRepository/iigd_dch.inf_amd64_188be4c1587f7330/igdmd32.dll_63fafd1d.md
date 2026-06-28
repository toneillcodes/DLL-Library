# Binary Specification: igdmd32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdmd32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `63fafd1dcf83d7805266f98b81fac217c2c0a56a561db7b6c3b70451baff8222`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseMetricsDevice` | `0x41AA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `OpenAdapterGroup` | `0x41B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OpenMetricsDevice` | `0x41B80` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `OpenMetricsDeviceFromFile` | `0x41CA0` | 3,896,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ClosePerformanceInterface` | `0x3F91A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `OpenPerformanceInterface` | `0x3F92D0` | 585,802 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
