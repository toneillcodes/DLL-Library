# Binary Specification: cldapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cldapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c6af6fcc072974e628984d35012220882f1198dd304566e735f24f24a22705d`
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
| 29 | `CfOpenFileWithOplock` | `0x3FD0` | 1,577 | UnwindData |  |
| 33 | `CfReferenceProtectedHandle` | `0x4EF0` | 42 | UnwindData |  |
| 35 | `CfReleaseProtectedHandle` | `0x4F20` | 4,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `CfReleaseTransferKey` | `0x4F20` | 4,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CfConnectSyncRoot` | `0x6170` | 3,402 | UnwindData |  |
| 9 | `CfDisconnectSyncRoot` | `0x6EC0` | 1,258 | UnwindData |  |
| 11 | `CfExecute` | `0x73B0` | 937 | UnwindData |  |
| 32 | `CfQuerySyncProviderStatus` | `0x7760` | 342 | UnwindData |  |
| 34 | `CfRegisterSyncRoot` | `0x78C0` | 5,166 | UnwindData |  |
| 39 | `CfReportSyncStatus` | `0x8D00` | 1,621 | UnwindData |  |
| 49 | `CfUnregisterSyncRoot` | `0x9360` | 907 | UnwindData |  |
| 51 | `CfUpdateSyncProviderStatus` | `0x9700` | 2,360 | UnwindData |  |
| 5 | `CfConvertToPlaceholder` | `0xF7E0` | 630 | UnwindData |  |
| 6 | `CfCreatePlaceholders` | `0xFA60` | 761 | UnwindData |  |
| 7 | `CfDehydratePlaceholder` | `0xFD60` | 33 | UnwindData |  |
| 8 | `CfDehydratePlaceholderEx` | `0xFD90` | 469 | UnwindData |  |
| 12 | `CfGetCorrelationVector` | `0xFF70` | 209 | UnwindData |  |
| 23 | `CfGetTransferKey` | `0x10050` | 259 | UnwindData |  |
| 25 | `CfHydratePlaceholder` | `0x10160` | 36 | UnwindData |  |
| 26 | `CfHydratePlaceholderWithAttributionPrivate` | `0x10190` | 352 | UnwindData |  |
| 41 | `CfRevertPlaceholder` | `0x10300` | 301 | UnwindData |  |
| 43 | `CfSetCorrelationVector` | `0x10440` | 376 | UnwindData |  |
| 44 | `CfSetInSyncState` | `0x105C0` | 402 | UnwindData |  |
| 45 | `CfSetPinState` | `0x10760` | 416 | UnwindData |  |
| 50 | `CfUpdatePlaceholder` | `0x10910` | 1,099 | UnwindData |  |
| 14 | `CfGetPlaceholderInfo` | `0x10D70` | 187 | UnwindData |  |
| 15 | `CfGetPlaceholderRangeInfo` | `0x10E40` | 165 | UnwindData |  |
| 16 | `CfGetPlaceholderRangeInfoForHydration` | `0x10EF0` | 2,056 | UnwindData |  |
| 20 | `CfGetPlatformInfo` | `0x11700` | 98 | UnwindData |  |
| 21 | `CfGetSyncRootInfoByHandle` | `0x11770` | 266 | UnwindData |  |
| 22 | `CfGetSyncRootInfoByPath` | `0x11880` | 265 | UnwindData |  |
| 27 | `CfLockProperties` | `0x11B70` | 216 | UnwindData |  |
| 40 | `CfRetrieveProperties` | `0x11C50` | 341 | UnwindData |  |
| 46 | `CfStoreProperties` | `0x11DB0` | 175 | UnwindData |  |
| 48 | `CfUnlockProperties` | `0x11E70` | 175 | UnwindData |  |
| 47 | `CfTestToggleSyncMsgThreadWaitEvent` | `0x12090` | 43,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CfGetPlaceholderStateFromAttributeTag` | `0x1CAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CfGetPlaceholderStateFromFileInfo` | `0x1CAE0` | 91 | UnwindData |  |
| 19 | `CfGetPlaceholderStateFromFindData` | `0x1CB50` | 2,669 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
