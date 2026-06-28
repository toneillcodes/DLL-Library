# Binary Specification: fstx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fstx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cd252f8c437e191f72a4ee284e25e7bf5dcb344f0ab6daa28c2e32944d545e3c`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 51 | `FsTxFree` | `0x65A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FsTxArmDisableByOperationIdTrigger` | `0x65D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FsTxArmNotificationDisableTrigger` | `0x65F0` | 69 | UnwindData |  |
| 8 | `FsTxCommitTransaction` | `0x6640` | 4,027 | UnwindData |  |
| 9 | `FsTxCopyFile` | `0x7610` | 535 | UnwindData |  |
| 10 | `FsTxCreateDirectory` | `0x7830` | 906 | UnwindData |  |
| 11 | `FsTxCreateDirectoryNT` | `0x7BC0` | 950 | UnwindData |  |
| 12 | `FsTxCreateFile` | `0x7F80` | 1,368 | UnwindData |  |
| 13 | `FsTxCreateFileNT` | `0x84E0` | 4,274 | UnwindData |  |
| 14 | `FsTxCreateGuid` | `0x95A0` | 662 | UnwindData |  |
| 15 | `FsTxCreateHardLink` | `0x9840` | 989 | UnwindData |  |
| 16 | `FsTxCreateHardLinkByHandle` | `0x9C30` | 982 | UnwindData |  |
| 17 | `FsTxCreateHardLinkByHandleNT` | `0xA010` | 990 | UnwindData |  |
| 18 | `FsTxCreateHardLinkNT` | `0xA400` | 931 | UnwindData |  |
| 21 | `FsTxDeInitGuidGenerator` | `0xAB90` | 503 | UnwindData |  |
| 22 | `FsTxDeleteDirectory` | `0xAD90` | 965 | UnwindData |  |
| 23 | `FsTxDeleteDirectoryByHandle` | `0xB160` | 968 | UnwindData |  |
| 24 | `FsTxDeleteDirectoryByHandleNT` | `0xB530` | 974 | UnwindData |  |
| 25 | `FsTxDeleteDirectoryNT` | `0xB910` | 971 | UnwindData |  |
| 26 | `FsTxDeleteFile` | `0xBCF0` | 972 | UnwindData |  |
| 27 | `FsTxDeleteFileByHandle` | `0xC0D0` | 1,001 | UnwindData |  |
| 28 | `FsTxDeleteFileByHandleNT` | `0xC4C0` | 1,023 | UnwindData |  |
| 29 | `FsTxDeleteFileNT` | `0xC8D0` | 978 | UnwindData |  |
| 30 | `FsTxDisarmDisableByOperationIdTrigger` | `0xD3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FsTxDisarmNotificationDisableTrigger` | `0xD3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `FsTxEnlistTransaction` | `0xD3C0` | 2,312 | UnwindData |  |
| 34 | `FsTxEnumTransactions` | `0xDCD0` | 668 | UnwindData |  |
| 35 | `FsTxFindClose` | `0xDF80` | 666 | UnwindData |  |
| 36 | `FsTxFindCloseNT` | `0xE220` | 807 | UnwindData |  |
| 39 | `FsTxFindFirstHardLink` | `0xE550` | 1,350 | UnwindData |  |
| 40 | `FsTxFindFirstHardLink2` | `0xEAA0` | 1,128 | UnwindData |  |
| 41 | `FsTxFindFirstHardLinkByHandle` | `0xEF10` | 1,040 | UnwindData |  |
| 42 | `FsTxFindFirstHardLinkByHandleNT` | `0xF330` | 908 | UnwindData |  |
| 43 | `FsTxFindFirstHardLinkNT` | `0xF6D0` | 5,612 | UnwindData |  |
| 44 | `FsTxFindHardLinkClose` | `0x10CD0` | 666 | UnwindData |  |
| 45 | `FsTxFindHardLinkCloseNT` | `0x10F70` | 941 | UnwindData |  |
| 47 | `FsTxFindNextHardLink` | `0x11330` | 1,158 | UnwindData |  |
| 48 | `FsTxFindNextHardLink2` | `0x117C0` | 947 | UnwindData |  |
| 49 | `FsTxFindNextHardLinkNT` | `0x11B80` | 1,405 | UnwindData |  |
| 54 | `FsTxGetEnlistmentCount` | `0x12110` | 51 | UnwindData |  |
| 55 | `FsTxGetFileAttributes` | `0x12150` | 1,030 | UnwindData |  |
| 56 | `FsTxGetFileAttributesByHandle` | `0x12560` | 1,052 | UnwindData |  |
| 57 | `FsTxGetFileAttributesByHandleNT` | `0x12990` | 1,036 | UnwindData |  |
| 58 | `FsTxGetFileAttributesNT` | `0x12DB0` | 1,062 | UnwindData |  |
| 59 | `FsTxGetNormalizedNameByHandleNT` | `0x131E0` | 881 | UnwindData |  |
| 63 | `FsTxInitGuidGenerator` | `0x13960` | 706 | UnwindData |  |
| 64 | `FsTxIsDefaultSessionContextSet` | `0x13D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `FsTxIsEnlistedTransaction` | `0x13D30` | 175 | UnwindData |  |
| 67 | `FsTxMoveDirectory` | `0x13DF0` | 2,270 | UnwindData |  |
| 68 | `FsTxMoveDirectoryNT` | `0x146E0` | 2,043 | UnwindData |  |
| 69 | `FsTxMoveFile` | `0x14EF0` | 1,618 | UnwindData |  |
| 70 | `FsTxMoveFileByHandle` | `0x15550` | 1,633 | UnwindData |  |
| 71 | `FsTxMoveFileByHandleNT` | `0x15BC0` | 1,629 | UnwindData |  |
| 72 | `FsTxMoveFileNT` | `0x16230` | 1,607 | UnwindData |  |
| 74 | `FsTxRollbackTransaction` | `0x16880` | 2,060 | UnwindData |  |
| 78 | `FsTxSetFileAttributes` | `0x170A0` | 943 | UnwindData |  |
| 79 | `FsTxSetFileAttributesByHandle` | `0x17460` | 1,001 | UnwindData |  |
| 80 | `FsTxSetFileAttributesByHandleNT` | `0x17850` | 1,008 | UnwindData |  |
| 81 | `FsTxSetFileAttributesNT` | `0x17C50` | 946 | UnwindData |  |
| 82 | `FsTxSetFileBasicInfo` | `0x18010` | 1,122 | UnwindData |  |
| 83 | `FsTxSetFileBasicInfoByHandle` | `0x18480` | 1,204 | UnwindData |  |
| 84 | `FsTxSetFileBasicInfoByHandleNT` | `0x18940` | 1,211 | UnwindData |  |
| 85 | `FsTxSetFileBasicInfoNT` | `0x18E10` | 1,127 | UnwindData |  |
| 86 | `FsTxSetPendingRenameRegValueName` | `0x19280` | 176 | UnwindData |  |
| 5 | `FsTxCloseHandle` | `0x33300` | 27 | UnwindData |  |
| 6 | `FsTxCloseHandleNT` | `0x33330` | 538 | UnwindData |  |
| 32 | `FsTxDuplicateHandleNT` | `0x33550` | 1,747 | UnwindData |  |
| 1 | `FsTxAlloc` | `0x35530` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FsTxCalloc` | `0x35560` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `FsTxMapWin32PathToNtPath` | `0x35B00` | 898 | UnwindData |  |
| 37 | `FsTxFindFileClose` | `0x36A60` | 54 | UnwindData |  |
| 38 | `FsTxFindFirstFile` | `0x36D80` | 1,168 | UnwindData |  |
| 46 | `FsTxFindNextFile` | `0x37710` | 14,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `FsTxGetSecurityInfoByHandleNT` | `0x3AF60` | 862 | UnwindData |  |
| 87 | `FsTxSetSecurityInfo` | `0x3B2D0` | 814 | UnwindData |  |
| 88 | `FsTxSetSecurityInfoByHandle` | `0x3B610` | 858 | UnwindData |  |
| 89 | `FsTxSetSecurityInfoByHandleNT` | `0x3B970` | 871 | UnwindData |  |
| 90 | `FsTxSetSecurityInfoNT` | `0x3BCE0` | 817 | UnwindData |  |
| 7 | `FsTxCloseSession` | `0x40B00` | 7,651 | UnwindData |  |
| 19 | `FsTxCreateRecoverySession` | `0x428F0` | 2,211 | UnwindData |  |
| 20 | `FsTxCreateSession` | `0x431A0` | 37 | UnwindData |  |
| 50 | `FsTxFindSessions` | `0x43B60` | 1,515 | UnwindData |  |
| 52 | `FsTxFreeSessionInfo` | `0x44160` | 549 | UnwindData |  |
| 53 | `FsTxFreeSessionList` | `0x44390` | 568 | UnwindData |  |
| 61 | `FsTxGetSessionId` | `0x445D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `FsTxGetSessionInfo` | `0x44600` | 1,483 | UnwindData |  |
| 73 | `FsTxPerformRecovery` | `0x44C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FsTxSetDefaultOplockLevels` | `0x44C30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `FsTxSetDefaultOplockLevelsNT` | `0x44C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `FsTxSetDefaultSession` | `0x44C90` | 107,490 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
