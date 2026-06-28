# Binary Specification: PeerDist.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PeerDist.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7f9f5469f803815c29211e1e9271fd68c356ab7d9b303f0d77d4aecab1001e00`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PeerDistClientAddContentInformation` | `0x3430` | 469 | UnwindData |  |
| 2 | `PeerDistClientAddData` | `0x3610` | 470 | UnwindData |  |
| 3 | `PeerDistClientBlockRead` | `0x37F0` | 493 | UnwindData |  |
| 4 | `PeerDistClientCancelAsyncOperation` | `0x39F0` | 472 | UnwindData |  |
| 5 | `PeerDistClientCloseContent` | `0x3BD0` | 477 | UnwindData |  |
| 6 | `PeerDistClientCompleteContentInformation` | `0x3DC0` | 459 | UnwindData |  |
| 7 | `PeerDistClientFlushContent` | `0x3FA0` | 453 | UnwindData |  |
| 8 | `PeerDistClientGetInformationByHandle` | `0x4170` | 434 | UnwindData |  |
| 9 | `PeerDistClientOpenContent` | `0x4330` | 426 | UnwindData |  |
| 10 | `PeerDistClientStreamRead` | `0x44E0` | 493 | UnwindData |  |
| 11 | `PeerDistGetOverlappedResult` | `0x46E0` | 162 | UnwindData |  |
| 12 | `PeerDistGetStatus` | `0x4790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `PeerDistGetStatusEx` | `0x47A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `PeerDistRegisterForStatusChangeNotification` | `0x47B0` | 31 | UnwindData |  |
| 15 | `PeerDistRegisterForStatusChangeNotificationEx` | `0x47E0` | 31 | UnwindData |  |
| 16 | `PeerDistServerCancelAsyncOperation` | `0x4810` | 429 | UnwindData |  |
| 17 | `PeerDistServerCloseContentInformation` | `0x49D0` | 422 | UnwindData |  |
| 18 | `PeerDistServerCloseStreamHandle` | `0x4B80` | 422 | UnwindData |  |
| 19 | `PeerDistServerOpenContentInformation` | `0x4D30` | 134 | UnwindData |  |
| 20 | `PeerDistServerOpenContentInformationEx` | `0x4DC0` | 78 | UnwindData |  |
| 21 | `PeerDistServerPublishAddToStream` | `0x4E20` | 470 | UnwindData |  |
| 22 | `PeerDistServerPublishCompleteStream` | `0x5000` | 459 | UnwindData |  |
| 23 | `PeerDistServerPublishStream` | `0x51E0` | 521 | UnwindData |  |
| 24 | `PeerDistServerRetrieveContentInformation` | `0x53F0` | 470 | UnwindData |  |
| 25 | `PeerDistServerUnpublish` | `0x55D0` | 429 | UnwindData |  |
| 26 | `PeerDistShutdown` | `0x5790` | 1,059 | UnwindData |  |
| 27 | `PeerDistStartup` | `0x5BC0` | 892 | UnwindData |  |
| 28 | `PeerDistUnregisterForStatusChangeNotification` | `0x5F50` | 391 | UnwindData |  |
