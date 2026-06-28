# Binary Specification: wimgapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wimgapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `27396695fa453a38ccb7d29894bde321ba266131e48de0131ef44c84867afabe`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `WIMAddImagePath` | `0x9740` | 1,464 | UnwindData |  |
| 50 | `WIMMountImageHandle` | `0xA510` | 3,409 | UnwindData |  |
| 29 | `WIMGetAttributes` | `0xD650` | 591 | UnwindData |  |
| 22 | `WIMExtractImagePath` | `0x1A4E0` | 21 | UnwindData |  |
| 25 | `WIMFindFirstImageFile` | `0x1B3E0` | 783 | UnwindData |  |
| 27 | `WIMFindNextImageFile` | `0x1B700` | 351 | UnwindData |  |
| 10 | `WIMCloseHandle` | `0x36DD0` | 142 | UnwindData |  |
| 13 | `WIMCreateFile` | `0x37360` | 3,179 | UnwindData |  |
| 31 | `WIMGetImageInformation` | `0x38B60` | 813 | UnwindData |  |
| 2 | `DllMain` | `0x4B250` | 48 | UnwindData |  |
| 57 | `WIMRegisterMessageCallback` | `0x4B310` | 375 | UnwindData |  |
| 30 | `WIMGetImageCount` | `0x4D7C0` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WIMSetTemporaryPath` | `0x4E3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `WIMLoadImage` | `0x4E400` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WIMInitFileIOCallbacks` | `0x4E4F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `WIMGetMountedImageHandle` | `0x4E5F0` | 407 | UnwindData |  |
| 73 | `WIMUnregisterMessageCallback` | `0x4F260` | 374 | UnwindData |  |
| 14 | `WIMCreateFileEx` | `0x53390` | 3,225 | UnwindData |  |
| 32 | `WIMGetInstanceCount` | `0x543C0` | 97 | UnwindData |  |
| 56 | `WIMRegisterLogFile` | `0x54440` | 513 | UnwindData |  |
| 47 | `WIMLoadInstance` | `0x55E60` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x56D60` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WIMAddImagePaths` | `0x570A0` | 847 | UnwindData |  |
| 5 | `WIMAddWimbootEntry` | `0x57750` | 384 | UnwindData |  |
| 39 | `WIMGetWIMBootEntries` | `0x578E0` | 466 | UnwindData |  |
| 40 | `WIMGetWIMBootWIMPath` | `0x57AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `WIMIsCurrentSystemWimboot` | `0x57AD0` | 211 | UnwindData |  |
| 74 | `WIMUpdateWIMBootEntry` | `0x57BB0` | 196 | UnwindData |  |
| 6 | `WIMApplyImage` | `0x58BD0` | 638 | UnwindData |  |
| 7 | `WIMApplyInstance` | `0x58E60` | 482 | UnwindData |  |
| 16 | `WIMCreateWofCompressedFile` | `0x59050` | 866 | UnwindData |  |
| 43 | `WIMInitializeWofDriver` | `0x593C0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `WIMRedirectFolderBeforeApply` | `0x59730` | 177 | UnwindData |  |
| 60 | `WIMSetCachedSigningLevel` | `0x597F0` | 7,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WIMCaptureImage` | `0x5B480` | 55 | UnwindData |  |
| 9 | `WIMCaptureInstance` | `0x5C8F0` | 69 | UnwindData |  |
| 48 | `WIMLoadOSInformation` | `0x5C940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `WIMSetImageUserSpecifiedCreationTime` | `0x5C950` | 91 | UnwindData |  |
| 67 | `WIMSetWimGuid` | `0x5C9C0` | 41 | UnwindData |  |
| 41 | `WIMGetWimFileSize` | `0x5D580` | 76 | UnwindData |  |
| 52 | `WIMReadFileEx` | `0x5D5E0` | 1,158 | UnwindData |  |
| 59 | `WIMSetBootImage` | `0x5DC30` | 355 | UnwindData |  |
| 65 | `WIMSetReferenceFile` | `0x5DDA0` | 533 | UnwindData |  |
| 11 | `WIMCommitImageHandle` | `0x5F300` | 821 | UnwindData |  |
| 18 | `WIMDeleteImageMounts` | `0x5F640` | 654 | UnwindData |  |
| 36 | `WIMGetMountedImageInfo` | `0x5F8E0` | 618 | UnwindData |  |
| 37 | `WIMGetMountedImageInfoFromHandle` | `0x5FB50` | 965 | UnwindData |  |
| 38 | `WIMGetMountedImages` | `0x600F0` | 208 | UnwindData |  |
| 49 | `WIMMountImage` | `0x601D0` | 691 | UnwindData |  |
| 58 | `WIMRemountImage` | `0x60490` | 652 | UnwindData |  |
| 70 | `WIMUnmountImage` | `0x60730` | 471 | UnwindData |  |
| 71 | `WIMUnmountImageHandle` | `0x60910` | 1,033 | UnwindData |  |
| 12 | `WIMCopyFile` | `0x61A60` | 2,881 | UnwindData |  |
| 75 | `WIMWriteFileWithIntegrity` | `0x626A0` | 1,388 | UnwindData |  |
| 15 | `WIMCreateImageFile` | `0x62E30` | 500 | UnwindData |  |
| 19 | `WIMEnumImageFiles` | `0x63030` | 564 | UnwindData |  |
| 26 | `WIMFindFirstInstanceFile` | `0x63270` | 681 | UnwindData |  |
| 28 | `WIMFindNextInstanceFile` | `0x63520` | 29 | UnwindData |  |
| 54 | `WIMReadInstanceFile` | `0x63520` | 29 | UnwindData |  |
| 45 | `WIMIsReferenceWim` | `0x63550` | 359 | UnwindData |  |
| 53 | `WIMReadImageFile` | `0x636C0` | 1,086 | UnwindData |  |
| 68 | `WIMSingleInstanceFile` | `0x63B10` | 614 | UnwindData |  |
| 17 | `WIMDeleteImage` | `0x63FA0` | 5,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WIMExportImage` | `0x654F0` | 3,884 | UnwindData |  |
| 21 | `WIMExtractImageDirectory` | `0x66E40` | 1,977 | UnwindData |  |
| 23 | `WIMExtractImagePathByWimHandle` | `0x67600` | 346 | UnwindData |  |
| 24 | `WIMExtractInstancePath` | `0x67760` | 21 | UnwindData |  |
| 33 | `WIMGetInstanceInformation` | `0x681D0` | 589 | UnwindData |  |
| 62 | `WIMSetImageInformation` | `0x68430` | 1,721 | UnwindData |  |
| 64 | `WIMSetInstanceInformation` | `0x68AF0` | 1,312 | UnwindData |  |
| 34 | `WIMGetMessageCallbackCount` | `0x6B220` | 133 | UnwindData |  |
| 61 | `WIMSetFileIOCallbackTemporaryPath` | `0x6B3E0` | 230 | UnwindData |  |
| 51 | `WIMProcessCustomImage` | `0x6F1B0` | 1,795 | UnwindData |  |
| 72 | `WIMUnregisterLogFile` | `0x6FD90` | 273 | UnwindData |  |
| 69 | `WIMSplitFile` | `0x6FEB0` | 1,806 | UnwindData |  |
