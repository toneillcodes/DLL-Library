# Binary Specification: wimgapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wimgapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10498a3abb0326bfa42fb65f07a884eb7e056452f7f47b059cc8b431cb6be526`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 29 | `WIMGetAttributes` | `0xA310` | 591 | UnwindData |  |
| 22 | `WIMExtractImagePath` | `0x16FB0` | 21 | UnwindData |  |
| 25 | `WIMFindFirstImageFile` | `0x17EB0` | 783 | UnwindData |  |
| 27 | `WIMFindNextImageFile` | `0x181D0` | 351 | UnwindData |  |
| 3 | `WIMAddImagePath` | `0x334B0` | 1,464 | UnwindData |  |
| 10 | `WIMCloseHandle` | `0x34F10` | 142 | UnwindData |  |
| 13 | `WIMCreateFile` | `0x354A0` | 3,179 | UnwindData |  |
| 31 | `WIMGetImageInformation` | `0x36CA0` | 813 | UnwindData |  |
| 50 | `WIMMountImageHandle` | `0x437B0` | 3,409 | UnwindData |  |
| 2 | `DllMain` | `0x4B370` | 48 | UnwindData |  |
| 57 | `WIMRegisterMessageCallback` | `0x4B430` | 375 | UnwindData |  |
| 30 | `WIMGetImageCount` | `0x4D8E0` | 2,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WIMSetTemporaryPath` | `0x4E350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `WIMLoadImage` | `0x4E360` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WIMInitFileIOCallbacks` | `0x4E450` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `WIMGetMountedImageHandle` | `0x4E580` | 407 | UnwindData |  |
| 73 | `WIMUnregisterMessageCallback` | `0x4F1F0` | 374 | UnwindData |  |
| 14 | `WIMCreateFileEx` | `0x53350` | 3,225 | UnwindData |  |
| 32 | `WIMGetInstanceCount` | `0x54380` | 97 | UnwindData |  |
| 56 | `WIMRegisterLogFile` | `0x54400` | 513 | UnwindData |  |
| 47 | `WIMLoadInstance` | `0x55E20` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x56D20` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WIMAddImagePaths` | `0x57060` | 847 | UnwindData |  |
| 5 | `WIMAddWimbootEntry` | `0x57710` | 384 | UnwindData |  |
| 39 | `WIMGetWIMBootEntries` | `0x578A0` | 466 | UnwindData |  |
| 40 | `WIMGetWIMBootWIMPath` | `0x57A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `WIMIsCurrentSystemWimboot` | `0x57A90` | 211 | UnwindData |  |
| 74 | `WIMUpdateWIMBootEntry` | `0x57B70` | 196 | UnwindData |  |
| 6 | `WIMApplyImage` | `0x58B90` | 638 | UnwindData |  |
| 7 | `WIMApplyInstance` | `0x58E20` | 482 | UnwindData |  |
| 16 | `WIMCreateWofCompressedFile` | `0x59010` | 866 | UnwindData |  |
| 43 | `WIMInitializeWofDriver` | `0x59380` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `WIMRedirectFolderBeforeApply` | `0x596F0` | 177 | UnwindData |  |
| 60 | `WIMSetCachedSigningLevel` | `0x597B0` | 7,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WIMCaptureImage` | `0x5B440` | 55 | UnwindData |  |
| 9 | `WIMCaptureInstance` | `0x5C8B0` | 69 | UnwindData |  |
| 48 | `WIMLoadOSInformation` | `0x5C900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `WIMSetImageUserSpecifiedCreationTime` | `0x5C910` | 91 | UnwindData |  |
| 67 | `WIMSetWimGuid` | `0x5C980` | 41 | UnwindData |  |
| 41 | `WIMGetWimFileSize` | `0x5D540` | 76 | UnwindData |  |
| 52 | `WIMReadFileEx` | `0x5D5A0` | 1,158 | UnwindData |  |
| 59 | `WIMSetBootImage` | `0x5DBF0` | 355 | UnwindData |  |
| 65 | `WIMSetReferenceFile` | `0x5DD60` | 533 | UnwindData |  |
| 11 | `WIMCommitImageHandle` | `0x5F2C0` | 821 | UnwindData |  |
| 18 | `WIMDeleteImageMounts` | `0x5F600` | 654 | UnwindData |  |
| 36 | `WIMGetMountedImageInfo` | `0x5F8A0` | 618 | UnwindData |  |
| 37 | `WIMGetMountedImageInfoFromHandle` | `0x5FB10` | 965 | UnwindData |  |
| 38 | `WIMGetMountedImages` | `0x600B0` | 208 | UnwindData |  |
| 49 | `WIMMountImage` | `0x60190` | 691 | UnwindData |  |
| 58 | `WIMRemountImage` | `0x60450` | 652 | UnwindData |  |
| 70 | `WIMUnmountImage` | `0x606F0` | 471 | UnwindData |  |
| 71 | `WIMUnmountImageHandle` | `0x608D0` | 1,033 | UnwindData |  |
| 12 | `WIMCopyFile` | `0x61A20` | 2,881 | UnwindData |  |
| 75 | `WIMWriteFileWithIntegrity` | `0x62660` | 1,388 | UnwindData |  |
| 15 | `WIMCreateImageFile` | `0x62DF0` | 500 | UnwindData |  |
| 19 | `WIMEnumImageFiles` | `0x62FF0` | 564 | UnwindData |  |
| 26 | `WIMFindFirstInstanceFile` | `0x63230` | 681 | UnwindData |  |
| 28 | `WIMFindNextInstanceFile` | `0x634E0` | 29 | UnwindData |  |
| 54 | `WIMReadInstanceFile` | `0x634E0` | 29 | UnwindData |  |
| 45 | `WIMIsReferenceWim` | `0x63510` | 359 | UnwindData |  |
| 53 | `WIMReadImageFile` | `0x63680` | 1,086 | UnwindData |  |
| 68 | `WIMSingleInstanceFile` | `0x63AD0` | 614 | UnwindData |  |
| 17 | `WIMDeleteImage` | `0x63F60` | 5,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WIMExportImage` | `0x654B0` | 3,884 | UnwindData |  |
| 21 | `WIMExtractImageDirectory` | `0x66E00` | 1,977 | UnwindData |  |
| 23 | `WIMExtractImagePathByWimHandle` | `0x675C0` | 346 | UnwindData |  |
| 24 | `WIMExtractInstancePath` | `0x67720` | 21 | UnwindData |  |
| 33 | `WIMGetInstanceInformation` | `0x68190` | 589 | UnwindData |  |
| 62 | `WIMSetImageInformation` | `0x683F0` | 1,721 | UnwindData |  |
| 64 | `WIMSetInstanceInformation` | `0x68AB0` | 1,312 | UnwindData |  |
| 34 | `WIMGetMessageCallbackCount` | `0x6B1E0` | 133 | UnwindData |  |
| 61 | `WIMSetFileIOCallbackTemporaryPath` | `0x6B3A0` | 230 | UnwindData |  |
| 51 | `WIMProcessCustomImage` | `0x6E650` | 1,795 | UnwindData |  |
| 72 | `WIMUnregisterLogFile` | `0x6F230` | 273 | UnwindData |  |
| 69 | `WIMSplitFile` | `0x6F350` | 1,806 | UnwindData |  |
