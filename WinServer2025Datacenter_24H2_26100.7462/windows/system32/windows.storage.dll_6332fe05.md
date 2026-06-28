# Binary Specification: windows.storage.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\windows.storage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6332fe058bf5aca37bc5f68e7535ddd6759909c14fa1b02d13489c934c152aa0`
* **Total Exported Functions:** 691

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `IsRemovableDevicePath` | `0xA910` | 43 | UnwindData |  |
| 459 | `SHGetFolderPathW` | `0x20030` | 32 | UnwindData |  |
| 458 | `SHGetFolderPathEx` | `0x202F0` | 21 | UnwindData |  |
| 466 | `SHGetKnownFolderIDList_Internal` | `0x21FB0` | 883 | UnwindData |  |
| 465 | `SHGetKnownFolderIDList` | `0x23260` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `SHGetKnownFolderItem` | `0x235A0` | 117 | UnwindData |  |
| 275 | `HideExtension` | `0x2E870` | 300 | UnwindData |  |
| 84 | `App_IsLFNAware` | `0x3FBC0` | 440 | UnwindData |  |
| 430 | `SHDefExtractIconW` | `0x41C30` | 834 | UnwindData |  |
| 88 | `AssocCreateStateRepoElement` | `0x44150` | 989 | UnwindData |  |
| 444 | `SHGetComputerDisplayName` | `0x46700` | 557 | UnwindData |  |
| 914 | *Ordinal Only* | `0x4B7A0` | 315 | UnwindData |  |
| 161 | `CreateSortColumnArray` | `0x4C0F0` | 194 | UnwindData |  |
| 212 | `GetCachedIniForFolder` | `0x4C700` | 228 | UnwindData |  |
| 645 | `SHChangeNotification_Unlock` | `0x4D5F0` | 9,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `CFreeThreadedItemContainer_CreateInstance` | `0x4F9A0` | 273 | UnwindData |  |
| 280 | `ILCloneFirst` | `0x51D20` | 228 | UnwindData |  |
| 414 | `SHCreateItemFromIDList` | `0x533C0` | 784 | UnwindData |  |
| 418 | `SHCreateItemWithParent` | `0x536E0` | 801 | UnwindData |  |
| 136 | `CShellItem_CreateInstance` | `0x53B10` | 78 | UnwindData |  |
| 415 | `SHCreateItemFromParsingName` | `0x5AC00` | 1,098 | UnwindData |  |
| 468 | `SHGetKnownFolderPath` | `0x5E400` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | *Ordinal Only* | `0x60EA0` | 302 | UnwindData |  |
| 2003 | *Ordinal Only* | `0x62080` | 10,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `GetRegDataDrivenCommandWithAssociation` | `0x649D0` | 253 | UnwindData |  |
| 850 | *Ordinal Only* | `0x656C0` | 43 | UnwindData |  |
| 421 | `SHCreateSessionKey` | `0x69B00` | 151 | UnwindData |  |
| 15 | `GetCurrentSessionId` | `0x69BA0` | 78 | UnwindData |  |
| 486 | `SHGetSpecialFolderPathW` | `0x6AAA0` | 540 | UnwindData |  |
| 479 | `SHGetPathFromIDListEx` | `0x6DE30` | 1,161 | UnwindData |  |
| 388 | `SHBindToFolderIDListParentEx` | `0x6E470` | 3,150 | UnwindData |  |
| 392 | `SHBindToParent` | `0x6FDC0` | 1,498 | UnwindData |  |
| 105 | `CDesktopFolder_CreateInstanceWithBindContext` | `0x73730` | 2,621 | UnwindData |  |
| 506 | `SHParseDisplayName` | `0x749E0` | 713 | UnwindData |  |
| 292 | `ILIsEqual` | `0x74E10` | 371 | UnwindData |  |
| 862 | *Ordinal Only* | `0x75080` | 394 | UnwindData |  |
| 448 | `SHGetDesktopFolder` | `0x75D40` | 1,879 | UnwindData |  |
| 389 | `SHBindToObject` | `0x764A0` | 2,926 | UnwindData |  |
| 109 | `CFSFolder_CreateFolder` | `0x77500` | 202 | UnwindData |  |
| 100 | `SHRestricted` | `0x77BE0` | 58 | UnwindData |  |
| 285 | `ILFindChild` | `0x7A500` | 524 | UnwindData |  |
| 494 | `SHILAliasTranslate` | `0x7AF50` | 1,958 | UnwindData |  |
| 332 | `NeverProvidedByJunction` | `0x7D6E0` | 34,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `SHGetItemFromObject` | `0x85BF0` | 152 | UnwindData |  |
| 433 | `SHExtCoCreateInstanceString` | `0x89D90` | 139 | UnwindData |  |
| 26 | `GetShellIconLocationParts` | `0x90FD0` | 227 | UnwindData |  |
| 487 | `SHGetStockIconInfo` | `0x910C0` | 317 | UnwindData |  |
| 24 | `GetShellIconLocation` | `0x91400` | 374 | UnwindData |  |
| 373 | `RebaseOnDriveLetter` | `0x96C30` | 558 | UnwindData |  |
| 351 | `PathIsLnk` | `0x97D50` | 65 | UnwindData |  |
| 346 | `PathIsBinaryExe` | `0x97DA0` | 113 | UnwindData |  |
| 318 | `IsNullTime` | `0x9A850` | 75 | UnwindData |  |
| 237 | `GetThreadFlags` | `0x9EE00` | 95 | UnwindData |  |
| 472 | `SHGetNameFromIDList` | `0xA19B0` | 126 | UnwindData |  |
| 174 | `DeserializeTextToLink` | `0xA3E00` | 268 | UnwindData |  |
| 358 | `PathIsSystemDrive` | `0xAF700` | 131 | UnwindData |  |
| 911 | *Ordinal Only* | `0xB0CF0` | 639 | UnwindData |  |
| 286 | `ILFindLastID` | `0xB3D40` | 17,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `DllGetClassObject` | `0xB8150` | 746 | UnwindData |  |
| 602 | `ShowSuperHidden` | `0xC2FF0` | 163 | UnwindData |  |
| 68 | `SHGetSetSettings` | `0xC3B90` | 446 | UnwindData |  |
| 297 | `IUnknown_GetFolderTargetIDList` | `0xCE430` | 428 | UnwindData |  |
| 4 | `SHChangeNotifyDeregister` | `0xD2470` | 260 | UnwindData |  |
| 2 | `SHChangeNotifyRegister` | `0xD26E0` | 399 | UnwindData |  |
| 395 | `SHChangeNotifyRegisterThread` | `0xD46E0` | 69 | UnwindData |  |
| 217 | `GetFindDataForPath` | `0xE8EC0` | 1,626 | UnwindData |  |
| 283 | `ILCreateFromPathEx` | `0xED9B0` | 168 | UnwindData |  |
| 151 | `CountFiles` | `0xEDBA0` | 86 | UnwindData |  |
| 361 | `PathIsWild` | `0xEDE20` | 57 | UnwindData |  |
| 271 | `GoModal` | `0xEF1D0` | 46 | UnwindData |  |
| 781 | *Ordinal Only* | `0xEFA00` | 172 | UnwindData |  |
| 315 | `IsLibraryPolicyEnabled` | `0xF24A0` | 110 | UnwindData |  |
| 460 | `SHGetIDListFromObject` | `0xF8840` | 164 | UnwindData |  |
| 279 | `ILClone` | `0xF9A70` | 39 | UnwindData |  |
| 512 | `SHQueryShellFolderValue` | `0xFC6D0` | 765 | UnwindData |  |
| 305 | `IsDelegateRegId` | `0xFE840` | 9,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `SHCreateDefaultExtractIcon` | `0x100BC0` | 198 | UnwindData |  |
| 348 | `PathIsEqualOrSubFolderOfKnownFolders` | `0x103C90` | 299 | UnwindData |  |
| 445 | `SHGetCorrectOwnerSid` | `0x103E60` | 1,602 | UnwindData |  |
| 347 | `PathIsEqualOrSubFolder` | `0x104990` | 336 | UnwindData |  |
| 308 | `IsElevationRequired` | `0x105080` | 295 | UnwindData |  |
| 349 | `PathIsExe` | `0x1053C0` | 113 | UnwindData |  |
| 495 | `SHIsCurrentThreadOnUserDesktop` | `0x105900` | 505 | UnwindData |  |
| 146 | `CheckSmartScreenWithAltFile` | `0x106D00` | 526 | UnwindData |  |
| 54 | `PathContainedByManifestedKnownFolder_FullTrustCaller_ForPackage` | `0x1116A0` | 1,528 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x112F50` | 315 | UnwindData |  |
| 11 | `CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x11EDE0` | 173 | UnwindData |  |
| 925 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x11EEA0` | 55 | UnwindData |  |
| 546 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x11EEA0` | 55 | UnwindData |  |
| 276 | `ICI2ICIX` | `0x122700` | 513 | UnwindData |  |
| 367 | `PathResolve` | `0x126D70` | 562 | UnwindData |  |
| 478 | `SHGetPathFromIDListAlloc` | `0x12DB40` | 899 | UnwindData |  |
| 394 | `SHChangeNotify` | `0x12DED0` | 1,065 | UnwindData |  |
| 27 | `ILSaveToStream` | `0x12EDB0` | 177 | UnwindData |  |
| 946 | `SHChangeNotifySuspendResume` | `0x12F910` | 174 | UnwindData |  |
| 791 | *Ordinal Only* | `0x139B90` | 61 | UnwindData |  |
| 788 | *Ordinal Only* | `0x13ACE0` | 591 | UnwindData |  |
| 817 | *Ordinal Only* | `0x13E850` | 267 | UnwindData |  |
| 376 | `RegGetValueString` | `0x13F190` | 200 | UnwindData |  |
| 114 | `CFolderExtractImage_Create` | `0x13FE90` | 249 | UnwindData |  |
| 344 | `PathGetPathDisplayName` | `0x140490` | 108 | UnwindData |  |
| 163 | `CreateVolatilePropertyStore` | `0x143BC0` | 196 | UnwindData |  |
| 943 | `CreateExtrinsicPropertyStore` | `0x1447B0` | 226 | UnwindData |  |
| 764 | *Ordinal Only* | `0x146300` | 1,984 | UnwindData |  |
| 581 | `SetLinkFlags` | `0x1537C0` | 173 | UnwindData |  |
| 158 | `CreateLinkFromItem` | `0x153910` | 371 | UnwindData |  |
| 416 | `SHCreateItemFromRelativeName` | `0x155020` | 313 | UnwindData |  |
| 157 | `CreateItemFromLink` | `0x167460` | 133 | UnwindData |  |
| 424 | `SHCreateShellItemArrayFromDataObject` | `0x16CF50` | 250 | UnwindData |  |
| 789 | *Ordinal Only* | `0x16DA20` | 163 | UnwindData |  |
| 135 | `CShellItemArray_CreateInstance` | `0x16DC50` | 123 | UnwindData |  |
| 425 | `SHCreateShellItemArrayFromIDLists` | `0x16DED0` | 149 | UnwindData |  |
| 134 | `CShellItemArrayWithCommonParent_CreateInstance` | `0x16ECF0` | 203 | UnwindData |  |
| 423 | `SHCreateShellItemArray` | `0x16F110` | 328 | UnwindData |  |
| 132 | `CShellItemArrayAsCollection_CreateInstance` | `0x16F260` | 203 | UnwindData |  |
| 8 | `CreateShellItemArrayFromAliasNamespaces` | `0x171140` | 612 | UnwindData |  |
| 866 | *Ordinal Only* | `0x172E10` | 46 | UnwindData |  |
| 397 | `SHCoCreateInstanceWorker` | `0x172E50` | 136 | UnwindData |  |
| 185 | `DoesBoundedItemArrayMatchAQS` | `0x174860` | 431 | UnwindData |  |
| 413 | `SHCreateFilterFromFullText` | `0x174B70` | 611 | UnwindData |  |
| 291 | `ILGetSize` | `0x1783F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `RegGetFirstShotQISearch` | `0x178420` | 273 | UnwindData |  |
| 825 | *Ordinal Only* | `0x179F50` | 204 | UnwindData |  |
| 847 | *Ordinal Only* | `0x17ADB0` | 296 | UnwindData |  |
| 330 | `MapIDListToIconILIndex` | `0x181530` | 179 | UnwindData |  |
| 873 | *Ordinal Only* | `0x1823C0` | 140 | UnwindData |  |
| 70 | `Shell_GetStockImageIndex` | `0x182C70` | 622 | UnwindData |  |
| 77 | *Ordinal Only* | `0x183AC0` | 77 | UnwindData |  |
| 393 | `SHBindWithFolder2Shim` | `0x183B20` | 186 | UnwindData |  |
| 490 | `SHGetUIObjectOfItem` | `0x184370` | 174 | UnwindData |  |
| 89 | `AssocGetDetailsOfPropKey` | `0x184510` | 359 | UnwindData |  |
| 461 | `SHGetImageList` | `0x185B90` | 189 | UnwindData |  |
| 79 | `_IsSHILInited` | `0x185FF0` | 52 | UnwindData |  |
| 55 | `QueryNewMaxIcons` | `0x187470` | 144 | UnwindData |  |
| 230 | `GetStartIndexFromUniqueNameTemplate` | `0x18BEA0` | 178 | UnwindData |  |
| 75 | `PathYetAnotherMakeUniqueName` | `0x18C780` | 336 | UnwindData |  |
| 342 | `PathFileExistsForUniqueName` | `0x18D0A0` | 371 | UnwindData |  |
| 412 | `SHCreateFileExtractIconW` | `0x18D4A0` | 263 | UnwindData |  |
| 159 | `CreateLinkToPidl` | `0x18D810` | 1,288 | UnwindData |  |
| 339 | `PathCleanupSpec` | `0x18E370` | 350 | UnwindData |  |
| 453 | `SHGetFileInfoW` | `0x18E4E0` | 654 | UnwindData |  |
| 281 | `ILCombine` | `0x193000` | 32 | UnwindData |  |
| 432 | `SHEvaluateSystemCommandTemplate` | `0x193DA0` | 28 | UnwindData |  |
| 575 | `SendNotificationsForLibraryItem` | `0x1967D0` | 244 | UnwindData |  |
| 846 | `ILLoadFromStreamEx` | `0x198FC0` | 305 | UnwindData |  |
| 482 | `SHGetSetFolderCustomSettings` | `0x19AB70` | 414 | UnwindData |  |
| 396 | `SHCloneSpecialIDList` | `0x19C370` | 72 | UnwindData |  |
| 484 | `SHGetSpecialFolderLocation` | `0x19C5E0` | 37 | UnwindData |  |
| 454 | `SHGetFolderLocation` | `0x19C610` | 395 | UnwindData |  |
| 497 | `SHKnownFolderFromCSIDL` | `0x19C7B0` | 4,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `CCachedShellItem_CreateInstance` | `0x19D920` | 237 | UnwindData |  |
| 295 | `ILRemoveLastID` | `0x19F2D0` | 23,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `StateRepoVerbsCache_GetContextMenuVerbs` | `0x1A4CD0` | 134 | UnwindData |  |
| 401 | `SHCreateDataObject` | `0x1A83F0` | 139 | UnwindData |  |
| 264 | *Ordinal Only* | `0x1A9070` | 302 | UnwindData |  |
| 740 | *Ordinal Only* | `0x1A9410` | 125 | UnwindData |  |
| 219 | `GetFolderString` | `0x1B1A50` | 225 | UnwindData |  |
| 71 | `TopViewDescription_GetGroupByProperty` | `0x1B71F0` | 107 | UnwindData |  |
| 851 | *Ordinal Only* | `0x1B78C0` | 159 | UnwindData |  |
| 823 | *Ordinal Only* | `0x1B7970` | 29 | UnwindData |  |
| 103 | `CCategoryProvider_CreateWithParams` | `0x1BB360` | 277 | UnwindData |  |
| 916 | *Ordinal Only* | `0x1D20B0` | 291 | UnwindData |  |
| 915 | *Ordinal Only* | `0x1D2730` | 800 | UnwindData |  |
| 385 | `SHAssocEnumHandlers` | `0x1D2BA0` | 133 | UnwindData |  |
| 399 | `SHCreateAssocHandler` | `0x1D2D90` | 68 | UnwindData |  |
| 322 | `IsProgramAccessEnabled` | `0x1D4CC0` | 400 | UnwindData |  |
| 180 | `DllMain` | `0x1D5BE0` | 414 | UnwindData |  |
| 52 | `IsUnderKnownFolder` | `0x1D9BC0` | 374 | UnwindData |  |
| 307 | `IsDesktopExplorerProcess` | `0x1E5550` | 34,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `GetSystemPersistedStorageItemList` | `0x1EDBA0` | 308 | UnwindData |  |
| 123 | `CItemStore_CreateInstance` | `0x1F0070` | 182 | UnwindData |  |
| 498 | `SHKnownFolderToCSIDL` | `0x1F0760` | 38 | UnwindData |  |
| 121 | `CItemSetOperations_CreateInstance` | `0x1F8B80` | 135 | UnwindData |  |
| 218 | `GetFindDataFromFileInformationByHandle` | `0x1FC570` | 380 | UnwindData |  |
| 387 | `SHBindToFolderIDListParent` | `0x1FC820` | 250 | UnwindData |  |
| 287 | `ILFree` | `0x1FFB50` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `SHFree` | `0x1FFB50` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `CRegFolder_CreateAndInit` | `0x2003C0` | 233 | UnwindData |  |
| 245 | `SHTestTokenMembership` | `0x203370` | 225 | UnwindData |  |
| 437 | `SHFileOperationWithAdditionalFlags` | `0x205800` | 524 | UnwindData |  |
| 345 | `PathGetShortPath` | `0x209A10` | 160 | UnwindData |  |
| 110 | `CFSFolder_IsCommonItem` | `0x20B5A0` | 25,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `Shell_GetCachedImageIndexW` | `0x211A70` | 239 | UnwindData |  |
| 611 | `Stream_ReadStringCoAllocW` | `0x2123E0` | 308 | UnwindData |  |
| 196 | `EnumShellItemsFromUnknown` | `0x215D80` | 489 | UnwindData |  |
| 613 | `Stream_WriteStringW` | `0x219130` | 154 | UnwindData |  |
| 147 | `SHCLSIDFromString` | `0x21B9E0` | 53 | UnwindData |  |
| 419 | `SHCreateItemWithParentAndChildId` | `0x21C8B0` | 168 | UnwindData |  |
| 492 | `SHGetUserDisplayName` | `0x21EC40` | 444 | UnwindData |  |
| 352 | `PathIsOneOf` | `0x223740` | 378 | UnwindData |  |
| 321 | `IsProcessAnExplorer` | `0x2381C0` | 140 | UnwindData |  |
| 33 | `GetUserChoiceForUrl` | `0x2394D0` | 952 | UnwindData |  |
| 143 | `CViewSettings_CreateInstance` | `0x23DE10` | 150 | UnwindData |  |
| 590 | `ShellExecuteExW` | `0x240330` | 255 | UnwindData |  |
| 577 | `SetAppStartingCursor` | `0x240FE0` | 191 | UnwindData |  |
| 164 | `CustomStatePropertyDescription_CreateWithItemPropertyStore` | `0x242F20` | 194 | UnwindData |  |
| 130 | `CRegFolder_CreateInstance` | `0x244560` | 200 | UnwindData |  |
| 426 | `SHCreateShellItemArrayFromShellItem` | `0x247790` | 277 | UnwindData |  |
| 250 | `Global_WindowsStorage_csIconCache` | `0x24A880` | 15,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `SHChangeNotification_Lock` | `0x24E470` | 128 | UnwindData |  |
| 489 | `SHGetUIObjectOf` | `0x24F0C0` | 161 | UnwindData |  |
| 405 | `SHCreateDelegatingTransfer` | `0x251EB0` | 164 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x255760` | 918 | UnwindData |  |
| 521 | `SHSetTemporaryPropertyForItem` | `0x2562F0` | 193 | UnwindData |  |
| 170 | `DataAccessCaches_InvalidateForLibrary` | `0x257BE0` | 63 | UnwindData |  |
| 377 | `RegistryVerbs_GetHandlerMultiSelectModel` | `0x2586A0` | 207 | UnwindData |  |
| 621 | `Win32RemoveDirectory` | `0x25F8F0` | 202 | UnwindData |  |
| 255 | `Global_WindowsStorage_fEndInitialized` | `0x2611F0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `CreateItemArrayFromObjectArray` | `0x2613D0` | 146 | UnwindData |  |
| 814 | *Ordinal Only* | `0x261830` | 153 | UnwindData |  |
| 765 | *Ordinal Only* | `0x263C40` | 230 | UnwindData |  |
| 830 | *Ordinal Only* | `0x264150` | 162 | UnwindData |  |
| 627 | `_PredictReasonableImpact` | `0x264E60` | 194 | UnwindData |  |
| 306 | `IsDesktopBandWindow` | `0x2668D0` | 82 | UnwindData |  |
| 86 | `AssocCreateForClasses` | `0x26A7F0` | 313 | UnwindData |  |
| 296 | `ILStreamSize` | `0x26A9E0` | 22,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | *Ordinal Only* | `0x270230` | 322 | UnwindData |  |
| 167 | `DAD_DragEnterEx` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `DAD_SetDragImage` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `DAD_ShowDragImage` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `IsLFNDriveA` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `IsLFNDriveW` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `SHShouldShowWizards` | `0x2724C0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `FilterOnAttributes` | `0x2729F0` | 13,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `SHGetFolderPathAndSubDirW` | `0x275DD0` | 270 | UnwindData |  |
| 290 | `ILGetNext` | `0x275EF0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | *Ordinal Only* | `0x276070` | 118 | UnwindData |  |
| 247 | `Global_WindowsStorage_Untyped_rgshil` | `0x2763F0` | 5,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `STORAGE_SHGetDesktopFolderWorker` | `0x277A50` | 10,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2001 | *Ordinal Only* | `0x27A1E0` | 164 | UnwindData |  |
| 815 | *Ordinal Only* | `0x27C1D0` | 51 | UnwindData |  |
| 609 | `StorageItemHelpers_IsSupportedRemovablePath` | `0x27EC20` | 40 | UnwindData |  |
| 257 | `Global_WindowsStorage_fIconCacheIsValid` | `0x280CA0` | 13,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `RebaseOnVolumeID` | `0x284220` | 600 | UnwindData |  |
| 317 | `IsNonEnumPolicySet` | `0x286240` | 185 | UnwindData |  |
| 254 | `Global_WindowsStorage_esServerMode` | `0x2889D0` | 9,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `Global_WindowsStorage_Untyped_MountPoint` | `0x28AFD0` | 3,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `SHGetSpecialFolderPathA` | `0x28BDB0` | 55 | UnwindData |  |
| 455 | `SHGetFolderPathA` | `0x28BDF0` | 146 | UnwindData |  |
| 428 | `SHCreateStdEnumFmtEtcEx` | `0x28F830` | 699 | UnwindData |  |
| 74 | `SHCreateStdEnumFmtEtc` | `0x28FB00` | 213 | UnwindData |  |
| 293 | `ILIsParent` | `0x291C60` | 25 | UnwindData |  |
| 216 | `GetFileUndoText` | `0x29CEB0` | 224 | UnwindData |  |
| 849 | *Ordinal Only* | `0x2A2890` | 43 | UnwindData |  |
| 248 | `Global_WindowsStorage_afNotRedirected` | `0x2A5780` | 10,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | *Ordinal Only* | `0x2A80F0` | 320 | UnwindData |  |
| 604 | `SplitFileNameAndExtension` | `0x2A8240` | 189 | UnwindData |  |
| 53 | `LoadNameTemplate` | `0x2A8310` | 289 | UnwindData |  |
| 249 | `Global_WindowsStorage_ccIcon` | `0x2AE3F0` | 16,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `GetFolderType` | `0x2B2390` | 1,869 | UnwindData |  |
| 223 | `GetRegDataDrivenCommand` | `0x2B5020` | 38 | UnwindData |  |
| 85 | `ArrangeWindows` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `DAD_AutoScroll` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `DllRegisterServer` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `DllUnregisterServer` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `InternalExtractIconListA` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `InternalExtractIconListW` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `IsValidIDList` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `IsValidIDListObject` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `SFVCB_OnAddPropertyPages` | `0x2B5C30` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `CTaskAddDoc_Create` | `0x2BA870` | 229 | UnwindData |  |
| 268 | `Global_WindowsStorage_tlsIconCache` | `0x2BAF50` | 4,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2009 | *Ordinal Only* | `0x2BC230` | 24,395 | UnwindData |  |
| 265 | `Global_WindowsStorage_lrFlags` | `0x2C5510` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetVolumeMountPath` | `0x2C5CD0` | 331 | UnwindData |  |
| 240 | `Global_WindowsStorage_Untyped_FileClassSRWLock` | `0x2C8360` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `TBCRegisterObjectParam` | `0x2C8890` | 268 | UnwindData |  |
| 80 | `_ustrcmp` | `0x2CFD10` | 57 | UnwindData |  |
| 144 | `CheckElevatedPermissionToShellItem` | `0x2D2260` | 713 | UnwindData |  |
| 383 | `SHAddIconsToCache` | `0x2D3C70` | 229 | UnwindData |  |
| 176 | `DetermineFolderDestinationParentAppID` | `0x2D5D20` | 648 | UnwindData |  |
| 480 | `SHGetPathFromIDListW` | `0x2D7BA0` | 162 | UnwindData |  |
| 2005 | *Ordinal Only* | `0x2D8F30` | 71 | UnwindData |  |
| 819 | *Ordinal Only* | `0x2DAB50` | 250 | UnwindData |  |
| 242 | `Global_WindowsStorage_Untyped_pFileClassCacheTable` | `0x2DD0D0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `GetShellClassInfoInfoTip` | `0x2DD430` | 90 | UnwindData |  |
| 227 | `GetShellClassInfo` | `0x2DD540` | 159 | UnwindData |  |
| 226 | `GetSelectionStateFromItemArray` | `0x2E1240` | 168 | UnwindData |  |
| 252 | `Global_WindowsStorage_dwThreadBindCtx` | `0x2E5CA0` | 5,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `PathIsTemporaryW` | `0x2E7280` | 66 | UnwindData |  |
| 253 | `Global_WindowsStorage_dwThreadInitializing` | `0x2E7CC0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `StateRepoVerbsCache_Destroy` | `0x2E8D20` | 37 | UnwindData |  |
| 104 | `CCollectionFactory_CreateInstance` | `0x2EACD0` | 288 | UnwindData |  |
| 120 | `CItemHandlerCache_CreateInstance` | `0x2EB750` | 173 | UnwindData |  |
| 2007 | *Ordinal Only* | `0x2EFDB0` | 21,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetFileSizeOnDisk` | `0x2F5270` | 92 | UnwindData |  |
| 6 | `AssocKeyFromElement` | `0x2F5420` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `SHHandleUpdateImage` | `0x2F5B50` | 137 | UnwindData |  |
| 313 | `IsLUAEnabled` | `0x2F5E10` | 75 | UnwindData |  |
| 562 | `STORAGE_SHCreateShellItemArrayFromDataObject` | `0x2FA520` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | *Ordinal Only* | `0x2FABD0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetThumbnailCutoffFromType` | `0x2FAE80` | 231 | UnwindData |  |
| 555 | `STORAGE_SHAddToRecentDocs` | `0x2FBDE0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `STORAGE_SHCreateShellItemArrayFromIDLists` | `0x2FBED0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | *Ordinal Only* | `0x2FC1E0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `Global_WindowsStorage_MaxIcons` | `0x2FCB50` | 3,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `STORAGE_SHCreateShellItemArray` | `0x2FD930` | 2,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `SetThreadFlags` | `0x2FE320` | 153 | UnwindData |  |
| 108 | `CFSFolder_AdjustForSlowColumn` | `0x2FEA70` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `STORAGE_SHCreateShellItemArrayFromShellItem` | `0x2FF2D0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `SHAddDefaultProperties` | `0x2FF8A0` | 352 | UnwindData |  |
| 139 | `CStorageItem_GetValidatedStorageItemObject` | `0x300410` | 156 | UnwindData |  |
| 64 | `SHGetCategorizer` | `0x303BC0` | 427 | UnwindData |  |
| 417 | `SHCreateItemInKnownFolder` | `0x3046B0` | 241 | UnwindData |  |
| 263 | `Global_WindowsStorage_lProcessClassCount` | `0x307C80` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `CFSTransfer_CreateInstance` | `0x308C50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `SHGetRealIDL` | `0x308CE0` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `CreateStorageItemFromShellItem` | `0x309950` | 8,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `STORAGE_AddItemToRecentDocs` | `0x30BBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `CPrivateProfileCache_Save` | `0x30BBE0` | 77 | UnwindData |  |
| 260 | `Global_WindowsStorage_iLastSysIcon` | `0x30BC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `STORAGE_SHFileOperation` | `0x30BC60` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `AssocShouldProcessUseAppToAppLaunching` | `0x30CED0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `IsUserAnAdmin` | `0x30D400` | 7,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `Global_WindowsStorage_iLastSystemColorDepth` | `0x30F1B0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `Global_WindowsStorage_fNeedsInitBroadcast` | `0x30F440` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `QueryStorageAccess_FullTrustCaller_ForToken` | `0x3100A0` | 310 | UnwindData |  |
| 548 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandleAndSecondaryStreamName` | `0x310B60` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `STORAGE_FillResultWithNullForKeys` | `0x310B60` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | *Ordinal Only* | `0x310B60` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `SHMapIDListToSystemImageListIndexAsync2` | `0x310E90` | 456 | UnwindData |  |
| 538 | `STORAGE_CStorageItem_GetValidatedStorageItem` | `0x312500` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `CreateStorageItemFromPath_PartialTrustCaller` | `0x313B70` | 174 | UnwindData |  |
| 551 | `STORAGE_GetShellItemFromStorageItem` | `0x314E10` | 4,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `ICIX2SEI` | `0x315E90` | 285 | UnwindData |  |
| 450 | `SHGetDiskFreeSpaceExW` | `0x318450` | 17,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `Global_WindowsStorage_fIconCacheHasBeenSuccessfullyCreated` | `0x31CA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `Global_WindowsStorage_Untyped_pFileHanderMap` | `0x31CA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `CShellItemArrayAsVirtualizedObjectArray_CreateInstance` | `0x31CA70` | 123 | UnwindData |  |
| 409 | `SHCreateDirectoryExW` | `0x31D1B0` | 10,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `SHCreateDirectoryExWStub` | `0x31D1B0` | 10,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `STORAGE_SHCreateDirectoryExWWorker` | `0x31D1B0` | 10,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `OpenRegStream` | `0x31F980` | 2,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `DestroyHashItemTable` | `0x3201B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `DllCanUnloadNow` | `0x320250` | 93 | UnwindData |  |
| 600 | `ShouldUseStorageProviderViews` | `0x3318F0` | 277 | UnwindData |  |
| 178 | `DllGetActivationFactory` | `0x332E50` | 516 | UnwindData |  |
| 210 | `FreeIconList` | `0x3478D0` | 13,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `InvalidateDriveType` | `0x3478D0` | 13,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `PathIsShortcutToProgram` | `0x34ACC0` | 507 | UnwindData |  |
| 354 | `PathIsShortcut` | `0x34AED0` | 92 | UnwindData |  |
| 502 | `SHMapIDListToSystemImageListIndexAsync` | `0x3530E0` | 86 | UnwindData |  |
| 93 | `BrokerAppSiloShellItemsForApplicationUserModelId` | `0x353A80` | 132 | UnwindData |  |
| 94 | `BrokerAppSiloShellItemsForPackageFamilyName` | `0x353B10` | 1,145 | UnwindData |  |
| 316 | `IsNameListedUnderKey` | `0x356EB0` | 361 | UnwindData |  |
| 443 | `SHGetCompressedFileSizeW` | `0x3572B0` | 240 | UnwindData |  |
| 112 | `CFileOperationRecorder_CreateInstance` | `0x357A50` | 163 | UnwindData |  |
| 549 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_UseImplicitFlagsAndPackage` | `0x35B0B0` | 6,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | *Ordinal Only* | `0x35CAE0` | 33 | UnwindData |  |
| 10 | `CreateStorageItemFromPath_FullTrustCaller` | `0x35DC50` | 26 | UnwindData |  |
| 542 | `STORAGE_CreateStorageItemFromPath_FullTrustCaller` | `0x35DC50` | 26 | UnwindData |  |
| 406 | `SHCreateDirectory` | `0x360540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `SHCreateDirectoryStub` | `0x360540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `STORAGE_SHCreateDirectory` | `0x360540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `Win32DeleteFile` | `0x360580` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `SHAssocEnumHandlersForProtocolByApplication` | `0x360610` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `Global_WindowsStorage_hwndSCN` | `0x3608F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `Global_WindowsStorage_nImageManagerVersion` | `0x360900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `Global_WindowsStorage_csSCN` | `0x360960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `Global_WindowsStorage_ulNextID` | `0x360980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `Global_WindowsStorage_tlsThreadFlags` | `0x360990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `Global_WindowsStorage_iUseLinkPrefix` | `0x3609A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `Global_WindowsStorage_tlsChangeClientProxy` | `0x3609E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SHGetUserNameW` | `0x360AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | *Ordinal Only* | `0x360AD0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | *Ordinal Only* | `0x360D30` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | *Ordinal Only* | `0x360DE0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `Window_IsLFNAware` | `0x361370` | 37 | UnwindData |  |
| 598 | `ShortSizeFormat64` | `0x361560` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `SHCreateDirectoryExA` | `0x3615F0` | 57,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `SHCreateDirectoryExAStub` | `0x3615F0` | 57,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `STORAGE_SHCreateDirectoryExA` | `0x3615F0` | 57,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | *Ordinal Only* | `0x36F4C0` | 863 | UnwindData |  |
| 816 | *Ordinal Only* | `0x36F830` | 160 | UnwindData |  |
| 844 | *Ordinal Only* | `0x36F8E0` | 156 | UnwindData |  |
| 87 | `AssocCreateListForClasses` | `0x3ACE60` | 190,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `GetCachedFileUpdateInformation` | `0x3DB830` | 18 | UnwindData |  |
| 945 | `GetInfoForFileInUse` | `0x3DFC60` | 89 | UnwindData |  |
| 233 | `GetSystemPersistedStorageItemListForUser` | `0x3DFE30` | 345 | UnwindData |  |
| 272 | `GrantPathAccess_FullTrustCaller_ForPackage` | `0x3DFF90` | 187 | UnwindData |  |
| 273 | `GrantWorkingDirectoryAccess_FullTrustCaller_ForPackage` | `0x3E0060` | 193 | UnwindData |  |
| 370 | `QueryStorageAccess_FullTrustCaller_ForPackage` | `0x3E0130` | 503 | UnwindData |  |
| 610 | `Storage_Internal_GetAccessListForPackage` | `0x3E0330` | 315 | UnwindData |  |
| 462 | `SHGetInstanceExplorer` | `0x3E0510` | 805,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ApplyProviderSettings` | `0x4A4FB0` | 201 | UnwindData |  |
| 14 | `GatherProviderSettings` | `0x4A5670` | 230 | UnwindData |  |
| 60 | `RegisterChangeNotifications` | `0x4A5910` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `UnregisterChangeNotifications` | `0x4A5CC0` | 3,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CreateLocalizationDesktopIni` | `0x4A6BF0` | 89 | UnwindData |  |
| 508 | `SHPrepareKnownFoldersCommon` | `0x4A6C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `SHPrepareKnownFoldersUser` | `0x4A6C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `SHSetKnownFolderPath` | `0x4A6C70` | 28,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | *Ordinal Only* | `0x4ADA80` | 52 | UnwindData |  |
| 150 | `CopyDefaultLibrariesFromGroupPolicy` | `0x4B17D0` | 250 | UnwindData |  |
| 314 | `IsLibraryCreatedByPolicy` | `0x4B18D0` | 388 | UnwindData |  |
| 514 | `SHResolveLibrary` | `0x4B5380` | 62 | UnwindData |  |
| 155 | `CreateItemArrayFromItemStore` | `0x4C1990` | 167 | UnwindData |  |
| 195 | `EnumShellItemsFromEnumFullIdList` | `0x4C1A40` | 175 | UnwindData |  |
| 427 | `SHCreateShellItemArrayWithFolderParent` | `0x4C1B90` | 165 | UnwindData |  |
| 124 | `CMruLongList_CreateInstance` | `0x4FF3D0` | 231 | UnwindData |  |
| 626 | `_CleanRecentDocs` | `0x506E00` | 679 | UnwindData |  |
| 947 | `CreateStorageProviderPropertyStore` | `0x5134B0` | 284 | UnwindData |  |
| 165 | `CustomStatePropertyDescription_CreateWithStateIdentifier` | `0x513940` | 171 | UnwindData |  |
| 213 | `GetCommandProviderForFolderType` | `0x520C10` | 124 | UnwindData |  |
| 456 | `SHGetFolderPathAndSubDirA` | `0x523F80` | 214 | UnwindData |  |
| 517 | `SHSetFolderPathA` | `0x524060` | 121 | UnwindData |  |
| 518 | `SHSetFolderPathW` | `0x5240E0` | 253 | UnwindData |  |
| 535 | `STORAGE_AddNewFolderToFrequentPlaces` | `0x5241F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `STORAGE_CEnumFiles_CreateInstance` | `0x524200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `STORAGE_CStatusProvider_CreateInstance` | `0x524210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `STORAGE_CStorageItem_GetValidatedStorageItemObject` | `0x524220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `STORAGE_ClearDestinationsForAllApps` | `0x524230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `STORAGE_CreateSortColumnArrayFromListDesc` | `0x524240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `STORAGE_CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x524250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `STORAGE_CreateStorageItemFromPath_PartialTrustCaller` | `0x524260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller` | `0x524270` | 26 | UnwindData |  |
| 547 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandle` | `0x524290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `STORAGE_GetSystemPersistedStorageItemList` | `0x5242A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `STORAGE_MakeDestinationItem` | `0x5242B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `STORAGE_PathIsEqualOrSubFolderOfKnownFolders` | `0x5242C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `STORAGE_SHAddToRecentDocsEx` | `0x5242D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `STORAGE_SHConfirmOperation` | `0x5242E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `STORAGE_SHFileOperationA` | `0x5242F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `STORAGE_SHFreeNameMappings` | `0x524300` | 98 | UnwindData |  |
| 569 | `STORAGE_SHGetPathFromMsUri` | `0x524370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `STORAGE_SHOpenFolderAndSelectItems` | `0x524380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `STORAGE_SHPathPrepareForWriteA` | `0x524390` | 114 | UnwindData |  |
| 572 | `STORAGE_SHPathPrepareForWriteW` | `0x524410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `STORAGE_SHValidateMSUri` | `0x524420` | 41,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `StateRepoVerbsCache_RebuildCacheAsync` | `0x52E4B0` | 122 | UnwindData |  |
| 1003 | *Ordinal Only* | `0x57C410` | 163 | UnwindData |  |
| 761 | *Ordinal Only* | `0x57C4C0` | 123 | UnwindData |  |
| 530 | `SHUpdateImageA` | `0x57C550` | 106 | UnwindData |  |
| 531 | `SHUpdateImageW` | `0x57C5C0` | 240 | UnwindData |  |
| 3 | `AllowRecycleBinOnVolume` | `0x57C780` | 319 | UnwindData |  |
| 13 | `EnsureRecycleBinLocation` | `0x57C960` | 168 | UnwindData |  |
| 16 | `GetDefaultMaxCapacity` | `0x57CA10` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetRecreatableRecycleBinLocation` | `0x57CC90` | 389 | UnwindData |  |
| 21 | `GetRecycleBinKey` | `0x57CE20` | 218 | UnwindData |  |
| 22 | `GetRecycleBinLocation` | `0x57CF00` | 211 | UnwindData |  |
| 23 | `GetRecycleBinPath` | `0x57CFE0` | 178 | UnwindData |  |
| 34 | `GetVolumeGUIDFromVolumeName` | `0x57D140` | 58 | UnwindData |  |
| 47 | `IsRecycleBinIconEmpty` | `0x57D230` | 348 | UnwindData |  |
| 48 | `IsRecycleBinKnownFolder` | `0x57D3A0` | 556 | UnwindData |  |
| 67 | `SHUpdateRecycleBinIconEx` | `0x57DCF0` | 70 | UnwindData |  |
| 510 | `SHQueryRecycleBinA` | `0x57E940` | 149 | UnwindData |  |
| 511 | `SHQueryRecycleBinW` | `0x57E9E0` | 323 | UnwindData |  |
| 532 | `SHUpdateRecycleBinIcon` | `0x57EB30` | 57 | UnwindData |  |
| 617 | `UpdateRecycleBinIcon` | `0x57EB70` | 1,563 | UnwindData |  |
| 7 | `BuildName` | `0x57F1A0` | 736 | UnwindData |  |
| 12 | `DrawTransparentBackground` | `0x57FEE0` | 334 | UnwindData |  |
| 18 | `GetMonitorRects` | `0x580450` | 221 | UnwindData |  |
| 19 | `GetPrimaryMonitor` | `0x5805E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `GetStringsFromFormat` | `0x580610` | 236 | UnwindData |  |
| 36 | `HrLoadString` | `0x5807F0` | 37 | UnwindData |  |
| 38 | `ImageList_GetMirrored` | `0x580820` | 127 | UnwindData |  |
| 39 | `ImageList_MirroredDraw` | `0x5808B0` | 164 | UnwindData |  |
| 40 | `InitDeletedItem` | `0x580960` | 115 | UnwindData |  |
| 43 | `IsFolderPicker` | `0x580C90` | 144 | UnwindData |  |
| 45 | `IsImmersivePicker` | `0x580D30` | 129 | UnwindData |  |
| 46 | `IsQueryCancelAutoplay` | `0x580E50` | 29 | UnwindData |  |
| 51 | `IsTSPerfFlagEnabled` | `0x580F00` | 280 | UnwindData |  |
| 62 | `SHCreateInfotipControl` | `0x582340` | 236 | UnwindData |  |
| 63 | `SHGetAttributesRequiringElevationFromDataObject` | `0x582440` | 708 | UnwindData |  |
| 66 | `SHInitializeInfotipControl` | `0x582710` | 205 | UnwindData |  |
| 72 | `UnInitDeletedItem` | `0x5828E0` | 62 | UnwindData |  |
| 81 | `AddCommas` | `0x583940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `AddCommasExportW` | `0x583950` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `CheckWinIniForAssocs` | `0x5839B0` | 1,057 | UnwindData |  |
| 880 | *Ordinal Only* | `0x583DE0` | 43 | UnwindData |  |
| 173 | `DeleteItemsInDataObject` | `0x583E20` | 357 | UnwindData |  |
| 194 | `EnableAndShowWindow` | `0x584040` | 63 | UnwindData |  |
| 211 | `FreeThreadIconCache` | `0x5841F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `GetDragImageMsg` | `0x584210` | 45 | UnwindData |  |
| 215 | `GetFileDescription` | `0x584250` | 109 | UnwindData |  |
| 221 | `GetIconLocationFromExt` | `0x5843A0` | 290 | UnwindData |  |
| 222 | `GetMsgPos` | `0x5844D0` | 40 | UnwindData |  |
| 225 | `GetSelectionFromSite` | `0x584500` | 153 | UnwindData |  |
| 229 | `GetShellItemsAsTextHGLOBAL` | `0x5845A0` | 523 | UnwindData |  |
| 231 | `GetStockIconIndexAndSystemIL` | `0x584960` | 231 | UnwindData |  |
| 234 | `GetTargetFromMergedFolderIDList` | `0x584B50` | 147 | UnwindData |  |
| 235 | `GetTargetItemFromMergedFolderIDList` | `0x584C90` | 114 | UnwindData |  |
| 236 | `GetTargetItemFromMergedFolderItem` | `0x584D10` | 114 | UnwindData |  |
| 238 | `GetThreadIconCache` | `0x584D90` | 266 | UnwindData |  |
| 299 | `Int64ToString` | `0x584F40` | 635 | UnwindData |  |
| 303 | `InvokeFolderPidl` | `0x5851D0` | 196 | UnwindData |  |
| 304 | `IsBlockedFromOpenWithBrowse` | `0x5852A0` | 25 | UnwindData |  |
| 309 | `IsExplorerBrowser` | `0x5852C0` | 91 | UnwindData |  |
| 310 | `IsExplorerModeBrowser` | `0x585330` | 114 | UnwindData |  |
| 319 | `IsOtherProcessAnExplorer` | `0x5853B0` | 112 | UnwindData |  |
| 320 | `IsPathOwnedByCurrentUser` | `0x585430` | 196 | UnwindData |  |
| 325 | `IsWindowInProcess` | `0x585500` | 85 | UnwindData |  |
| 326 | `ItemIsSystemDrive` | `0x585560` | 105 | UnwindData |  |
| 327 | `LargeIntegerToString` | `0x5855D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `MenuCharMatch` | `0x5855E0` | 171 | UnwindData |  |
| 335 | `ParseField` | `0x5856A0` | 443 | UnwindData |  |
| 336 | `ParsePrinterName` | `0x585870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `ParsePrinterNameEx` | `0x585880` | 216 | UnwindData |  |
| 340 | `PathComposeWithArgs` | `0x585960` | 108 | UnwindData |  |
| 368 | `PathSeperateArgs` | `0x5859E0` | 211 | UnwindData |  |
| 369 | `QueryCancelAutoPlayMsg` | `0x585AC0` | 90 | UnwindData |  |
| 378 | `ReplaceSearchIDListScope` | `0x585B20` | 549 | UnwindData |  |
| 390 | `SHBindToObjectByName` | `0x585D50` | 132 | UnwindData |  |
| 391 | `SHBindToObjectWithMode` | `0x585DE0` | 126 | UnwindData |  |
| 402 | `SHCreateDataObjectFromShellItemsOrFolder` | `0x585E70` | 309 | UnwindData |  |
| 431 | `SHEnumerateUnreadMailAccountsW` | `0x5861A0` | 250 | UnwindData |  |
| 436 | `SHFileOperationEx` | `0x5862A0` | 412 | UnwindData |  |
| 438 | `SHFindComputer` | `0x586450` | 202 | UnwindData |  |
| 90 | `SHFindFiles` | `0x586520` | 208 | UnwindData |  |
| 750 | *Ordinal Only* | `0x586600` | 378 | UnwindData |  |
| 477 | `SHGetPathFromIDListA` | `0x586780` | 333 | UnwindData |  |
| 491 | `SHGetUnreadMailCountW` | `0x5868E0` | 647 | UnwindData |  |
| 496 | `SHIsFileAvailableOffline` | `0x586B70` | 436 | UnwindData |  |
| 499 | `SHLaunchSearch` | `0x586D30` | 247 | UnwindData |  |
| 500 | `SHLoadNonloadedIconOverlayIdentifiers` | `0x586E30` | 29 | UnwindData |  |
| 522 | `SHSetUnreadMailCountW` | `0x586E60` | 555 | UnwindData |  |
| 523 | `SHSettingsChanged` | `0x5870A0` | 97 | UnwindData |  |
| 525 | `SHSimpleIDListFromPath` | `0x587110` | 95 | UnwindData |  |
| 526 | `SHSimulateDropOnClsid` | `0x587180` | 153 | UnwindData |  |
| 527 | `SHSysErrorMessageBox` | `0x587220` | 412 | UnwindData |  |
| 529 | `SHTrackPopupMenu` | `0x5873D0` | 373 | UnwindData |  |
| 574 | `SVIDFromViewMode` | `0x587550` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `SetExplorerServerMode` | `0x5875D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `Shell_MergeMenus` | `0x5875E0` | 845 | UnwindData |  |
| 599 | `ShortSizeFormatExportW` | `0x587940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `ShowElevationPromptSuppressedError` | `0x587960` | 180 | UnwindData |  |
| 603 | `SimulateDropWithPasteSucceeded` | `0x587A20` | 195 | UnwindData |  |
| 612 | `Stream_ReadStringW` | `0x587C90` | 166 | UnwindData |  |
| 615 | `TransferDelete` | `0x587E20` | 316 | UnwindData |  |
| 618 | `ViewModeFromSVID` | `0x587F70` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CreateStorageHandlerViaMoniker` | `0x588560` | 299 | UnwindData |  |
| 25 | `GetShellIconLocationCommaIndex` | `0x588F70` | 129 | UnwindData |  |
| 29 | `GetStockIcon` | `0x589000` | 120 | UnwindData |  |
| 31 | `GetSystemImageListBitDepth` | `0x589080` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `IsIconResourcePath` | `0x589110` | 400 | UnwindData |  |
| 50 | `IsShell32IconStock` | `0x589470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `Shell32IconToShell32ExtractIconParameter` | `0x5894B0` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `FileIconInitIfNeeded` | `0x589E00` | 27 | UnwindData |  |
| 429 | `SHDefExtractIconA` | `0x589ED0` | 142 | UnwindData |  |
| 592 | `Shell_GetCachedImageIndex` | `0x589F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `Shell_GetCachedImageIndexA` | `0x589F80` | 108 | UnwindData |  |
| 595 | `Shell_GetImageLists` | `0x58A000` | 117 | UnwindData |  |
| 597 | `Shell_SysColorChange` | `0x58A080` | 179 | UnwindData |  |
| 37 | `IItemCategorizer_SetCategories` | `0x58C870` | 428 | UnwindData |  |
| 97 | `CAlphabeticalCategorizer_CreateInstance` | `0x58ED00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CCategorizerFactory_CreateInstance` | `0x58ED20` | 139 | UnwindData |  |
| 102 | `CCategoryProvider_CreateInstance` | `0x58EDC0` | 188 | UnwindData |  |
| 106 | `CDriveSizeCategorizer_CreateInstance` | `0x58EF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `CDriveTypeCategorizer_CreateInstance` | `0x58EF50` | 155 | UnwindData |  |
| 117 | `CFreeSpaceCategorizer_CreateInstance` | `0x58F000` | 59 | UnwindData |  |
| 125 | `CPercentCategorizer_CreateInstance` | `0x58F1D0` | 52 | UnwindData |  |
| 128 | `CRatingsCategorizer_CreateInstance` | `0x58F310` | 176 | UnwindData |  |
| 138 | `CSizeCategorizer_CreateInstance` | `0x58F3D0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `CTimeCategorizer_CreateInstance` | `0x58F580` | 42 | UnwindData |  |
| 910 | *Ordinal Only* | `0x58F5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `Install_AdvancedShellSettings` | `0x58F5C0` | 69 | UnwindData |  |
| 483 | `SHGetSettings` | `0x58FA20` | 103 | UnwindData |  |
| 56 | `RealShellExecuteA` | `0x5925A0` | 8,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `RealShellExecuteExA` | `0x5925A0` | 8,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RealShellExecuteExW` | `0x5925A0` | 8,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RealShellExecuteW` | `0x5925A0` | 8,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `SHCreateProcessAsUserW` | `0x594700` | 29 | UnwindData |  |
| 586 | `ShellExec_RunDLLA` | `0x594730` | 162 | UnwindData |  |
| 587 | `ShellExec_RunDLLW` | `0x5947E0` | 343 | UnwindData |  |
| 588 | `ShellExecuteA` | `0x594940` | 132 | UnwindData |  |
| 589 | `ShellExecuteExA` | `0x5949D0` | 218 | UnwindData |  |
| 591 | `ShellExecuteW` | `0x594AB0` | 158 | UnwindData |  |
| 619 | `WOWShellExecute` | `0x594B60` | 286 | UnwindData |  |
| 61 | `ResolveShortNameCollisions` | `0x596B90` | 430 | UnwindData |  |
| 141 | `CTaskEnumHKCR_Create` | `0x599510` | 177 | UnwindData |  |
| 476 | `SHGetNoAssocIconIndex` | `0x5995D0` | 10,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `VerifySaferTrust` | `0x59BDA0` | 460 | UnwindData |  |
| 207 | `FindExecutableA` | `0x59C430` | 208 | UnwindData |  |
| 208 | `FindExecutableW` | `0x59C510` | 416 | UnwindData |  |
| 311 | `IsImmersiveUICaller` | `0x59C6C0` | 190 | UnwindData |  |
| 533 | `SHValidateUNC` | `0x59C800` | 375 | UnwindData |  |
| 583 | `ShellExecCmdLine` | `0x59C980` | 49 | UnwindData |  |
| 584 | `ShellExecCmdLineWithSite` | `0x59C9C0` | 552 | UnwindData |  |
| 585 | `ShellExecPidl` | `0x59CBF0` | 404 | UnwindData |  |
| 83 | `AddHashItem` | `0x59CD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `CreateHashItemTable` | `0x59CDB0` | 86 | UnwindData |  |
| 171 | `DeleteHashItem` | `0x59CE10` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `FindHashItem` | `0x59CEF0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_CalculateHashKey` | `0x59D270` | 90 | UnwindData |  |
| 91 | `AssocGetPropListForExt` | `0x5A0250` | 253 | UnwindData |  |
| 441 | `SHGetAssocKeys` | `0x5A0360` | 337 | UnwindData |  |
| 442 | `SHGetAssocKeysForIDList` | `0x5A04C0` | 132 | UnwindData |  |
| 96 | `BuildUniqueLinkName` | `0x5A1D00` | 203 | UnwindData |  |
| 384 | `SHAlloc` | `0x5A1F30` | 39 | UnwindData |  |
| 172 | *Ordinal Only* | `0x5A1F60` | 39 | UnwindData |  |
| 898 | *Ordinal Only* | `0x5A1F90` | 413 | UnwindData |  |
| 422 | `SHCreateShellItem` | `0x5A2140` | 62 | UnwindData |  |
| 446 | `SHGetDataFromIDListA` | `0x5A2190` | 277 | UnwindData |  |
| 447 | `SHGetDataFromIDListW` | `0x5A22B0` | 391 | UnwindData |  |
| 449 | `SHGetDiskFreeSpaceExA` | `0x5A2440` | 115 | UnwindData |  |
| 451 | `SHGetFileIcon` | `0x5A24C0` | 135 | UnwindData |  |
| 452 | `SHGetFileInfoA` | `0x5A2550` | 308 | UnwindData |  |
| 463 | `SHGetItemFromDataObject` | `0x5A2690` | 114 | UnwindData |  |
| 469 | `SHGetLocalizedName` | `0x5A2710` | 161 | UnwindData |  |
| 470 | `SHGetLocalizedNameAlloc` | `0x5A27C0` | 235 | UnwindData |  |
| 471 | `SHGetMalloc` | `0x5A28C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `SHGetNewLinkInfoA` | `0x5A28E0` | 273 | UnwindData |  |
| 475 | `SHGetNewLinkInfoW` | `0x5A2A00` | 34 | UnwindData |  |
| 243 | *Ordinal Only* | `0x5A2A30` | 134 | UnwindData |  |
| 244 | *Ordinal Only* | `0x5A2AC0` | 140 | UnwindData |  |
| 488 | `SHGetTemporaryPropertyForItem` | `0x5A2B60` | 193 | UnwindData |  |
| 501 | `SHMapIDListToSystemImageListIndex` | `0x5A2C30` | 26 | UnwindData |  |
| 513 | `SHRemoveLocalizedName` | `0x5A2C50` | 148 | UnwindData |  |
| 520 | `SHSetLocalizedName` | `0x5A2CF0` | 243 | UnwindData |  |
| 98 | `CApplyPropertiesUndoUnit_CreateInstance` | `0x5A3920` | 134 | UnwindData |  |
| 113 | `CFilterEventSink_CreateInstance` | `0x5A4C80` | 185 | UnwindData |  |
| 622 | `WrapSinkAndAdviseCollection` | `0x5A4DE0` | 184 | UnwindData |  |
| 623 | `WrapSinkAndAdviseItem` | `0x5A4EA0` | 184 | UnwindData |  |
| 115 | `CFolderInfoTip_CreateInstance` | `0x5A5C20` | 135 | UnwindData |  |
| 116 | `CFolderShortcut_CreateInstance` | `0x5A9890` | 121 | UnwindData |  |
| 119 | `CINIPropSetStg_CreateInstance` | `0x5AB4B0` | 31 | UnwindData |  |
| 122 | `CItemStoreFilter_CreateInstance` | `0x5ACF00` | 13,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CPinnedPeopleList_CreateInstance` | `0x5B04F0` | 215 | UnwindData |  |
| 131 | `CSecurityEditor_CreateInstance` | `0x5B24E0` | 149 | UnwindData |  |
| 137 | `CSidResolver_CreateInstance` | `0x5B2580` | 207 | UnwindData |  |
| 515 | `SHResolveUserNames` | `0x5B2700` | 393 | UnwindData |  |
| 145 | `CheckEscapesW` | `0x5B2A30` | 191 | UnwindData |  |
| 338 | `PathAppend` | `0x5B2B00` | 81 | UnwindData |  |
| 341 | `PathFileExists` | `0x5B2B60` | 69 | UnwindData |  |
| 343 | `PathGetMountPointFromPath` | `0x5B2BB0` | 285 | UnwindData |  |
| 350 | `PathIsExeStub` | `0x5B2CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `PathIsRoot` | `0x5B2CF0` | 67 | UnwindData |  |
| 356 | `PathIsSlowA` | `0x5B2D40` | 90 | UnwindData |  |
| 357 | `PathIsSlowW` | `0x5B2DA0` | 145 | UnwindData |  |
| 359 | `PathIsTemporaryA` | `0x5B2E40` | 83 | UnwindData |  |
| 362 | `PathMakePretty` | `0x5B2EA0` | 104 | UnwindData |  |
| 363 | `PathMakeUniqueName` | `0x5B2F10` | 39 | UnwindData |  |
| 364 | `PathQualify` | `0x5B2F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `PathQualifyDef` | `0x5B2F60` | 825 | UnwindData |  |
| 366 | `PathRemoveFileSpec` | `0x5B32A0` | 67 | UnwindData |  |
| 149 | `ConvertStrings` | `0x5B3390` | 348 | UnwindData |  |
| 152 | `CreateDisplayNameRemapTransferSource` | `0x5B4C90` | 228 | UnwindData |  |
| 154 | `CreateInfoTipFromItem` | `0x5B5AD0` | 36 | UnwindData |  |
| 183 | `DoEnvironmentSubstA` | `0x5B5DE0` | 161 | UnwindData |  |
| 184 | `DoEnvironmentSubstW` | `0x5B5E90` | 163 | UnwindData |  |
| 186 | `DragAcceptFiles` | `0x5B5FD0` | 78 | UnwindData |  |
| 187 | `DragFinish` | `0x5B6030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `DragQueryFileA` | `0x5B6050` | 28 | UnwindData |  |
| 189 | `DragQueryFileAorW` | `0x5B6080` | 713 | UnwindData |  |
| 190 | `DragQueryFileW` | `0x5B6350` | 25 | UnwindData |  |
| 191 | `DragQueryInfo` | `0x5B6370` | 433 | UnwindData |  |
| 192 | `DragQueryPoint` | `0x5B6530` | 126 | UnwindData |  |
| 193 | `DuplicateIcon` | `0x5B65C0` | 139 | UnwindData |  |
| 197 | `ExtractAssociatedIconA` | `0x5B6660` | 249 | UnwindData |  |
| 198 | `ExtractAssociatedIconExA` | `0x5B6760` | 242 | UnwindData |  |
| 199 | `ExtractAssociatedIconExW` | `0x5B6860` | 605 | UnwindData |  |
| 200 | `ExtractAssociatedIconW` | `0x5B6AD0` | 178 | UnwindData |  |
| 201 | `ExtractIconA` | `0x5B6B90` | 123 | UnwindData |  |
| 202 | `ExtractIconExA` | `0x5B6C20` | 117 | UnwindData |  |
| 203 | `ExtractIconExW` | `0x5B6CA0` | 534 | UnwindData |  |
| 204 | `ExtractIconW` | `0x5B6EC0` | 216 | UnwindData |  |
| 435 | `SHExtractIconsW` | `0x5B7120` | 68 | UnwindData |  |
| 274 | `HIDA_ILClone` | `0x5B7600` | 87 | UnwindData |  |
| 278 | `ILAppendID` | `0x5B7660` | 266 | UnwindData |  |
| 282 | `ILCreateFromPathA` | `0x5B7770` | 126 | UnwindData |  |
| 284 | `ILCreateFromPathW` | `0x5B7800` | 71 | UnwindData |  |
| 288 | `ILGetDisplayName` | `0x5B7850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `ILGetDisplayNameEx` | `0x5B7870` | 254 | UnwindData |  |
| 294 | `ILIsParentByPath` | `0x5B7980` | 313 | UnwindData |  |
| 28 | `SHILCreateFromPath` | `0x5B7AC0` | 29 | UnwindData |  |
| 528 | `SHTestTokenPrivilegeW` | `0x5B7C60` | 184 | UnwindData |  |
| 328 | `LookupFileClassAdorner` | `0x5B8040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `LookupFileClassTypeOverlay` | `0x5B8050` | 22 | UnwindData |  |
| 379 | `ResetFileClassIcon` | `0x5B8070` | 137 | UnwindData |  |
| 579 | `SetFileClassAdorner` | `0x5B8100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `SetFileClassTypeOverlay` | `0x5B8120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `OldReadCabinetState` | `0x5B8140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `ReadCabinetState` | `0x5B8150` | 545 | UnwindData |  |
| 624 | `WriteCabinetState` | `0x5B8380` | 365 | UnwindData |  |
| 473 | `SHGetNetResource` | `0x5B86B0` | 397 | UnwindData |  |
| 504 | `SHNetConnectionDialog` | `0x5B8850` | 246 | UnwindData |  |
| 382 | `SHAddDefaultPropertiesByExt` | `0x5B8CD0` | 177 | UnwindData |  |
| 404 | `SHCreateDefaultPropertiesOp` | `0x5B8D90` | 300 | UnwindData |  |
| 516 | `SHSetDefaultProperties` | `0x5B8ED0` | 240 | UnwindData |  |
| 887 | *Ordinal Only* | `0x5B9910` | 297 | UnwindData |  |
| 434 | `SHExtCoCreateLocalServerLowIL` | `0x5B9A40` | 278 | UnwindData |  |
| 507 | `SHPinDllOfCLSIDStr` | `0x5B9B60` | 81 | UnwindData |  |
| 398 | `SHCopyStreamWithProgress` | `0x5B9BC0` | 25 | UnwindData |  |
| 400 | `SHCreateAssociationRegistration` | `0x5BF220` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | *Ordinal Only* | `0x5C06D0` | 133 | UnwindData |  |
| 439 | `SHFlushSFCache` | `0x5C07C0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `StgMakeUniqueName` | `0x5C0B30` | 311 | UnwindData |  |
| 616 | `TryBrokerSHBrowseForFolder` | `0x5C0ED0` | 504 | UnwindData |  |
| 298 | `IUnknown_ResolveItem` | `0x5E7960` | 138 | UnwindData |  |
| 576 | `SerializeLinkToText` | `0x5E79F0` | 293 | UnwindData |  |
| 505 | `SHOpenFolderAndSelectItems` | `0x5E9810` | 539 | UnwindData |  |
