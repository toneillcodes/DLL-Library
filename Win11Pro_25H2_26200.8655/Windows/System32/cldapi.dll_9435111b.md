# Binary Specification: cldapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cldapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9435111be8cfba3f0b881ad512a54a8cb18f6c3f09af4951e99ea4760b3747dd`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CfAbortOperation` | `0x28D0` | 1,550 | UnwindData |  |
| 13 | `CfGetLastSyncStatus` | `0x2EF0` | 132 | UnwindData |  |
| 30 | `CfOpenProgressEvent` | `0x2F80` | 181 | UnwindData |  |
| 31 | `CfQueryProgress` | `0x3040` | 1,197 | UnwindData |  |
| 37 | `CfReportProviderProgress` | `0x3500` | 31 | UnwindData |  |
| 38 | `CfReportProviderProgress2` | `0x3530` | 1,627 | UnwindData |  |
| 2 | `CfCloseAppPolicy` | `0x3BA0` | 27 | UnwindData |  |
| 10 | `CfEnumAppPolicy` | `0x3BD0` | 591 | UnwindData |  |
| 28 | `CfOpenAppPolicy` | `0x3E30` | 151 | UnwindData |  |
| 42 | `CfSetAppPolicy` | `0x3ED0` | 159 | UnwindData |  |
| 3 | `CfCloseHandle` | `0x3F80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CfGetWin32HandleFromProtectedHandle` | `0x3FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `CfOpenFileWithOplock` | `0x3FD0` | 2,357 | UnwindData |  |
| 33 | `CfReferenceProtectedHandle` | `0x4910` | 42 | UnwindData |  |
| 35 | `CfReleaseProtectedHandle` | `0x4940` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `CfReleaseTransferKey` | `0x4940` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CfConnectSyncRoot` | `0x5050` | 3,402 | UnwindData |  |
| 9 | `CfDisconnectSyncRoot` | `0x5DA0` | 1,258 | UnwindData |  |
| 11 | `CfExecute` | `0x6290` | 937 | UnwindData |  |
| 32 | `CfQuerySyncProviderStatus` | `0x6640` | 342 | UnwindData |  |
| 34 | `CfRegisterSyncRoot` | `0x67A0` | 5,166 | UnwindData |  |
| 39 | `CfReportSyncStatus` | `0x7BE0` | 1,621 | UnwindData |  |
| 49 | `CfUnregisterSyncRoot` | `0x8240` | 907 | UnwindData |  |
| 51 | `CfUpdateSyncProviderStatus` | `0x85E0` | 2,360 | UnwindData |  |
| 5 | `CfConvertToPlaceholder` | `0xE6C0` | 602 | UnwindData |  |
| 6 | `CfCreatePlaceholders` | `0xE920` | 761 | UnwindData |  |
| 7 | `CfDehydratePlaceholder` | `0xEC20` | 33 | UnwindData |  |
| 8 | `CfDehydratePlaceholderEx` | `0xEC50` | 469 | UnwindData |  |
| 12 | `CfGetCorrelationVector` | `0xEE30` | 209 | UnwindData |  |
| 23 | `CfGetTransferKey` | `0xEF10` | 259 | UnwindData |  |
| 25 | `CfHydratePlaceholder` | `0xF020` | 36 | UnwindData |  |
| 26 | `CfHydratePlaceholderWithAttributionPrivate` | `0xF050` | 352 | UnwindData |  |
| 41 | `CfRevertPlaceholder` | `0xF1C0` | 301 | UnwindData |  |
| 43 | `CfSetCorrelationVector` | `0xF300` | 376 | UnwindData |  |
| 44 | `CfSetInSyncState` | `0xF480` | 402 | UnwindData |  |
| 45 | `CfSetPinState` | `0xF620` | 416 | UnwindData |  |
| 50 | `CfUpdatePlaceholder` | `0xF7D0` | 1,099 | UnwindData |  |
| 14 | `CfGetPlaceholderInfo` | `0xFC30` | 187 | UnwindData |  |
| 15 | `CfGetPlaceholderRangeInfo` | `0xFD00` | 165 | UnwindData |  |
| 16 | `CfGetPlaceholderRangeInfoForHydration` | `0xFDB0` | 2,056 | UnwindData |  |
| 20 | `CfGetPlatformInfo` | `0x105C0` | 85 | UnwindData |  |
| 21 | `CfGetSyncRootInfoByHandle` | `0x10620` | 266 | UnwindData |  |
| 22 | `CfGetSyncRootInfoByPath` | `0x10730` | 265 | UnwindData |  |
| 27 | `CfLockProperties` | `0x11380` | 216 | UnwindData |  |
| 40 | `CfRetrieveProperties` | `0x11460` | 341 | UnwindData |  |
| 46 | `CfStoreProperties` | `0x115C0` | 175 | UnwindData |  |
| 48 | `CfUnlockProperties` | `0x11680` | 175 | UnwindData |  |
| 47 | `CfTestToggleSyncMsgThreadWaitEvent` | `0x118A0` | 42,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CfGetPlaceholderStateFromAttributeTag` | `0x1BEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CfGetPlaceholderStateFromFileInfo` | `0x1BEF0` | 140 | UnwindData |  |
| 19 | `CfGetPlaceholderStateFromFindData` | `0x1BF90` | 3,101 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
