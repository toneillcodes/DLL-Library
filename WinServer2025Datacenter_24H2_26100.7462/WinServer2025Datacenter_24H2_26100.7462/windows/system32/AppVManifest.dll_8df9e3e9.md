# Binary Specification: AppVManifest.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppVManifest.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8df9e3e91ad69c66feffd1da4f3391efb3a5f38f62f693b44aaf9e4f7b02c38b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateManifestDocumentFromDocument` | `0x3A670` | 384 | UnwindData |  |
| 3 | `CreateManifestDocumentFromFile` | `0x3A800` | 576 | UnwindData |  |
| 4 | `CreateManifestDocumentFromXML` | `0x3AA50` | 496 | UnwindData |  |
| 1 | `GetManifestSelectionNamespaces` | `0x3AC50` | 81,228 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
