# Binary Specification: DnnlPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\DnnlPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c32df65f9e6a22d625dbdd6429b2705ef21d5c423350ef7397cf885d141ace8f`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `GetPooling` | `0x66A0` | 110,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetPoolingAlt` | `0x216D0` | 33,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ReleaseMemory` | `0x29910` | 29,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ReleaseEngine` | `0x30D80` | 42,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetConvolutionAlt` | `0x3B3E0` | 49,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetConvolution` | `0x473F0` | 41,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SetEngine` | `0x517B0` | 10,754,502 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
