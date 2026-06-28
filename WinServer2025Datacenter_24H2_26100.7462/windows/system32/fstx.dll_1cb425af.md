# Binary Specification: fstx.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fstx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1cb425af7d10d11dd5767fafe2ea694d1aa61a3b6ec3cdee669e63698b8cb249`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 51 | `FsTxFree` | `0x65E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FsTxArmDisableByOperationIdTrigger` | `0x6610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FsTxArmNotificationDisableTrigger` | `0x6630` | 69 | UnwindData |  |
| 8 | `FsTxCommitTransaction` | `0x6680` | 4,027 | UnwindData |  |
| 9 | `FsTxCopyFile` | `0x7650` | 535 | UnwindData |  |
| 10 | `FsTxCreateDirectory` | `0x7870` | 906 | UnwindData |  |
| 11 | `FsTxCreateDirectoryNT` | `0x7C00` | 950 | UnwindData |  |
| 12 | `FsTxCreateFile` | `0x7FC0` | 1,368 | UnwindData |  |
| 13 | `FsTxCreateFileNT` | `0x8520` | 4,295 | UnwindData |  |
| 14 | `FsTxCreateGuid` | `0x95F0` | 662 | UnwindData |  |
| 15 | `FsTxCreateHardLink` | `0x9890` | 989 | UnwindData |  |
| 16 | `FsTxCreateHardLinkByHandle` | `0x9C80` | 982 | UnwindData |  |
| 17 | `FsTxCreateHardLinkByHandleNT` | `0xA060` | 990 | UnwindData |  |
| 18 | `FsTxCreateHardLinkNT` | `0xA450` | 931 | UnwindData |  |
| 21 | `FsTxDeInitGuidGenerator` | `0xABE0` | 503 | UnwindData |  |
| 22 | `FsTxDeleteDirectory` | `0xADE0` | 965 | UnwindData |  |
| 23 | `FsTxDeleteDirectoryByHandle` | `0xB1B0` | 968 | UnwindData |  |
| 24 | `FsTxDeleteDirectoryByHandleNT` | `0xB580` | 974 | UnwindData |  |
| 25 | `FsTxDeleteDirectoryNT` | `0xB960` | 971 | UnwindData |  |
| 26 | `FsTxDeleteFile` | `0xBD40` | 972 | UnwindData |  |
| 27 | `FsTxDeleteFileByHandle` | `0xC120` | 1,001 | UnwindData |  |
| 28 | `FsTxDeleteFileByHandleNT` | `0xC510` | 1,023 | UnwindData |  |
| 29 | `FsTxDeleteFileNT` | `0xC920` | 978 | UnwindData |  |
| 30 | `FsTxDisarmDisableByOperationIdTrigger` | `0xD3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FsTxDisarmNotificationDisableTrigger` | `0xD400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `FsTxEnlistTransaction` | `0xD410` | 2,312 | UnwindData |  |
| 34 | `FsTxEnumTransactions` | `0xDD20` | 668 | UnwindData |  |
| 35 | `FsTxFindClose` | `0xDFD0` | 666 | UnwindData |  |
| 36 | `FsTxFindCloseNT` | `0xE270` | 807 | UnwindData |  |
| 39 | `FsTxFindFirstHardLink` | `0xE5A0` | 1,350 | UnwindData |  |
| 40 | `FsTxFindFirstHardLink2` | `0xEAF0` | 1,128 | UnwindData |  |
| 41 | `FsTxFindFirstHardLinkByHandle` | `0xEF60` | 1,040 | UnwindData |  |
| 42 | `FsTxFindFirstHardLinkByHandleNT` | `0xF380` | 908 | UnwindData |  |
| 43 | `FsTxFindFirstHardLinkNT` | `0xF720` | 5,612 | UnwindData |  |
| 44 | `FsTxFindHardLinkClose` | `0x10D20` | 666 | UnwindData |  |
| 45 | `FsTxFindHardLinkCloseNT` | `0x10FC0` | 941 | UnwindData |  |
| 47 | `FsTxFindNextHardLink` | `0x11380` | 1,158 | UnwindData |  |
| 48 | `FsTxFindNextHardLink2` | `0x11810` | 947 | UnwindData |  |
| 49 | `FsTxFindNextHardLinkNT` | `0x11BD0` | 1,405 | UnwindData |  |
| 54 | `FsTxGetEnlistmentCount` | `0x12160` | 51 | UnwindData |  |
| 55 | `FsTxGetFileAttributes` | `0x121A0` | 1,030 | UnwindData |  |
| 56 | `FsTxGetFileAttributesByHandle` | `0x125B0` | 1,052 | UnwindData |  |
| 57 | `FsTxGetFileAttributesByHandleNT` | `0x129E0` | 1,036 | UnwindData |  |
| 58 | `FsTxGetFileAttributesNT` | `0x12E00` | 1,062 | UnwindData |  |
| 59 | `FsTxGetNormalizedNameByHandleNT` | `0x13230` | 881 | UnwindData |  |
| 63 | `FsTxInitGuidGenerator` | `0x139B0` | 706 | UnwindData |  |
| 64 | `FsTxIsDefaultSessionContextSet` | `0x13D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `FsTxIsEnlistedTransaction` | `0x13D80` | 175 | UnwindData |  |
| 67 | `FsTxMoveDirectory` | `0x13E40` | 2,270 | UnwindData |  |
| 68 | `FsTxMoveDirectoryNT` | `0x14730` | 2,043 | UnwindData |  |
| 69 | `FsTxMoveFile` | `0x14F40` | 1,618 | UnwindData |  |
| 70 | `FsTxMoveFileByHandle` | `0x155A0` | 1,633 | UnwindData |  |
| 71 | `FsTxMoveFileByHandleNT` | `0x15C10` | 1,629 | UnwindData |  |
| 72 | `FsTxMoveFileNT` | `0x16280` | 1,607 | UnwindData |  |
| 74 | `FsTxRollbackTransaction` | `0x168D0` | 2,060 | UnwindData |  |
| 78 | `FsTxSetFileAttributes` | `0x170F0` | 943 | UnwindData |  |
| 79 | `FsTxSetFileAttributesByHandle` | `0x174B0` | 1,001 | UnwindData |  |
| 80 | `FsTxSetFileAttributesByHandleNT` | `0x178A0` | 1,008 | UnwindData |  |
| 81 | `FsTxSetFileAttributesNT` | `0x17CA0` | 946 | UnwindData |  |
| 82 | `FsTxSetFileBasicInfo` | `0x18060` | 1,122 | UnwindData |  |
| 83 | `FsTxSetFileBasicInfoByHandle` | `0x184D0` | 1,204 | UnwindData |  |
| 84 | `FsTxSetFileBasicInfoByHandleNT` | `0x18990` | 1,211 | UnwindData |  |
| 85 | `FsTxSetFileBasicInfoNT` | `0x18E60` | 1,127 | UnwindData |  |
| 86 | `FsTxSetPendingRenameRegValueName` | `0x192D0` | 176 | UnwindData |  |
| 5 | `FsTxCloseHandle` | `0x335B0` | 27 | UnwindData |  |
| 6 | `FsTxCloseHandleNT` | `0x335E0` | 538 | UnwindData |  |
| 32 | `FsTxDuplicateHandleNT` | `0x33800` | 1,747 | UnwindData |  |
| 1 | `FsTxAlloc` | `0x357E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FsTxCalloc` | `0x35810` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `FsTxMapWin32PathToNtPath` | `0x35DB0` | 898 | UnwindData |  |
| 37 | `FsTxFindFileClose` | `0x36E50` | 54 | UnwindData |  |
| 38 | `FsTxFindFirstFile` | `0x37170` | 1,168 | UnwindData |  |
| 46 | `FsTxFindNextFile` | `0x37B00` | 14,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `FsTxGetSecurityInfoByHandleNT` | `0x3B360` | 862 | UnwindData |  |
| 87 | `FsTxSetSecurityInfo` | `0x3B6D0` | 814 | UnwindData |  |
| 88 | `FsTxSetSecurityInfoByHandle` | `0x3BA10` | 858 | UnwindData |  |
| 89 | `FsTxSetSecurityInfoByHandleNT` | `0x3BD70` | 871 | UnwindData |  |
| 90 | `FsTxSetSecurityInfoNT` | `0x3C0E0` | 817 | UnwindData |  |
| 7 | `FsTxCloseSession` | `0x40F00` | 7,651 | UnwindData |  |
| 19 | `FsTxCreateRecoverySession` | `0x42CF0` | 2,211 | UnwindData |  |
| 20 | `FsTxCreateSession` | `0x435A0` | 37 | UnwindData |  |
| 50 | `FsTxFindSessions` | `0x43F60` | 1,515 | UnwindData |  |
| 52 | `FsTxFreeSessionInfo` | `0x44560` | 549 | UnwindData |  |
| 53 | `FsTxFreeSessionList` | `0x44790` | 568 | UnwindData |  |
| 61 | `FsTxGetSessionId` | `0x449D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `FsTxGetSessionInfo` | `0x44A00` | 1,483 | UnwindData |  |
| 73 | `FsTxPerformRecovery` | `0x45020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FsTxSetDefaultOplockLevels` | `0x45030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `FsTxSetDefaultOplockLevelsNT` | `0x45060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `FsTxSetDefaultSession` | `0x45090` | 111,586 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
