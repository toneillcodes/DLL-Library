# Binary Specification: igdmd64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdmd64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `705acb25818bdffdd327f8a1b93c8763ab19884a7b04c19fa83fd5b946d2ef33`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseMetricsDevice` | `0x29C50` | 23 | UnwindData |  |
| 3 | `OpenAdapterGroup` | `0x29D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OpenMetricsDevice` | `0x29D50` | 28 | UnwindData |  |
| 5 | `OpenMetricsDeviceFromFile` | `0x29EB0` | 363 | UnwindData |  |
| 2 | `ClosePerformanceInterface` | `0x779960` | 70 | UnwindData |  |
| 6 | `OpenPerformanceInterface` | `0x779AC0` | 111 | UnwindData |  |
