# Binary Specification: combase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\combase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `82d8d2467a17fdea4693058247da34da140258df4ee7361043904bd565b4d0fe`
* **Total Exported Functions:** 608

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 159 | *Ordinal Only* | `0x6DD0` | 769 | UnwindData |  |
| 607 | `WindowsTrimStringEnd` | `0x98D0` | 278 | UnwindData |  |
| 600 | `WindowsIsStringEmpty` | `0xADC0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `WindowsCreateStringReference` | `0xB440` | 317 | UnwindData |  |
| 593 | `WindowsDeleteString` | `0xFF20` | 93 | UnwindData |  |
| 259 | `CoCreateFreeThreadedMarshaler` | `0x13E60` | 25 | UnwindData |  |
| 153 | *Ordinal Only* | `0x14B60` | 881 | UnwindData |  |
| 459 | `HSTRING_UserUnmarshal` | `0x15670` | 587 | UnwindData |  |
| 601 | `WindowsPreallocateStringBuffer` | `0x167A0` | 302 | UnwindData |  |
| 595 | `WindowsDuplicateString` | `0x168E0` | 103 | UnwindData |  |
| 591 | `WindowsCreateString` | `0x16EB0` | 75 | UnwindData |  |
| 559 | `RoOriginateErrorW` | `0x17370` | 365 | UnwindData |  |
| 548 | `RoGetActivationFactory` | `0x193A0` | 295 | UnwindData |  |
| 113 | `CLSIDFromProgID` | `0x1BD90` | 369 | UnwindData |  |
| 542 | `RoActivateInstance` | `0x1D070` | 412 | UnwindData |  |
| 352 | `CoTaskMemAlloc` | `0x21330` | 78 | UnwindData |  |
| 596 | `WindowsGetStringLen` | `0x305C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `WindowsPromoteStringBuffer` | `0x305E0` | 127 | UnwindData |  |
| 560 | `RoOriginateLanguageException` | `0x307F0` | 126 | UnwindData |  |
| 549 | `RoGetAgileReference` | `0x34AB0` | 1,880 | UnwindData |  |
| 531 | `IsErrorPropagationEnabled` | `0x35650` | 36 | UnwindData |  |
| 164 | *Ordinal Only* | `0x37170` | 534 | UnwindData |  |
| 122 | *Ordinal Only* | `0x3C7D0` | 73 | UnwindData |  |
| 572 | `RoUninitialize` | `0x3CE30` | 15 | UnwindData |  |
| 357 | `CoUninitialize` | `0x3CE50` | 764 | UnwindData |  |
| 308 | `CoInitializeEx` | `0x3D180` | 336 | UnwindData |  |
| 532 | `NdrCStdStubBuffer2_Release` | `0x3EB50` | 217 | UnwindData |  |
| 533 | `NdrCStdStubBuffer_Release` | `0x3EB50` | 217 | UnwindData |  |
| 353 | `CoTaskMemFree` | `0x3F7F0` | 83 | UnwindData |  |
| 87 | *Ordinal Only* | `0x468D0` | 362 | UnwindData |  |
| 364 | `CoWaitForMultipleHandles` | `0x47940` | 253 | UnwindData |  |
| 335 | `CoReleaseMarshalData` | `0x4BF00` | 587 | UnwindData |  |
| 243 | `CStdStubBuffer_DebugServerRelease` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `HACCEL_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `HACCEL_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `HBRUSH_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `HBRUSH_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `HDC_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `HICON_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `HICON_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `HMENU_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `HMENU_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `HMONITOR_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `HMONITOR_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `HRGN_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `HWND_UserFree` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `HWND_UserFree64` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `InternalFreeObjRef` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `InternalSetOleThunkWowPtr` | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | *Ordinal Only* | `0x506E0` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `StringFromCLSID` | `0x58D60` | 436 | UnwindData |  |
| 540 | `PropVariantCopy` | `0x5A060` | 12 | UnwindData |  |
| 321 | `CoQueryClientBlanket` | `0x5B7C0` | 171 | UnwindData |  |
| 168 | *Ordinal Only* | `0x5BB70` | 231 | UnwindData |  |
| 184 | *Ordinal Only* | `0x5BC60` | 574 | UnwindData |  |
| 167 | *Ordinal Only* | `0x5C070` | 396 | UnwindData |  |
| 306 | `CoImpersonateClient` | `0x5C210` | 1,094 | UnwindData |  |
| 339 | `CoRevertToSelf` | `0x5C660` | 1,068 | UnwindData |  |
| 280 | `CoGetCallContext` | `0x5CAA0` | 686 | UnwindData |  |
| 317 | `CoMarshalInterface` | `0x6D090` | 1,808 | UnwindData |  |
| 360 | `CoUnmarshalInterface` | `0x6D940` | 1,992 | UnwindData |  |
| 521 | `InternalRegisterWindowPropInterface2` | `0x7AC70` | 418 | UnwindData |  |
| 337 | `CoResumeClassObjects` | `0x7CCE0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `CoRevokeClassObject` | `0x7D290` | 65 | UnwindData |  |
| 272 | `CoDisconnectObject` | `0x7D570` | 605 | UnwindData |  |
| 336 | `CoReleaseServerProcess` | `0x7E970` | 5,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | *Ordinal Only* | `0x800C0` | 10,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x82B80` | 181 | UnwindData |  |
| 260 | `CoCreateGuid` | `0x8AE10` | 100 | UnwindData |  |
| 245 | `CStdStubBuffer_Invoke` | `0x8DC20` | 428 | UnwindData |  |
| 288 | `CoGetCurrentLogicalThreadId` | `0x91AF0` | 65 | UnwindData |  |
| 480 | `InternalCStdIdentityGetIProxyManager` | `0x93710` | 23,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `CoUnloadingWOW` | `0x99180` | 6,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | *Ordinal Only* | `0x9AB90` | 184 | UnwindData |  |
| 111 | *Ordinal Only* | `0x9AE50` | 72 | UnwindData |  |
| 576 | `SetRestrictedErrorInfo` | `0x9CAB0` | 152 | UnwindData |  |
| 176 | *Ordinal Only* | `0x9CB50` | 281 | UnwindData |  |
| 380 | `GetRestrictedErrorInfo` | `0x9CC70` | 268 | UnwindData |  |
| 347 | `CoSetErrorInfo` | `0x9D4B0` | 263 | UnwindData |  |
| 575 | `SetErrorInfo` | `0x9D4B0` | 263 | UnwindData |  |
| 553 | `RoGetParameterizedTypeInstanceIID` | `0xA10C0` | 392 | UnwindData |  |
| 590 | `WindowsConcatString` | `0xA2390` | 479 | UnwindData |  |
| 535 | `NdrOleDllGetClassObject` | `0xA7F00` | 121 | UnwindData |  |
| 302 | `CoGetStandardMarshal` | `0xAF6C0` | 1,201 | UnwindData |  |
| 299 | `CoGetObjectContext` | `0xAFB80` | 100 | UnwindData |  |
| 578 | `StringFromGUID2` | `0xB6370` | 33 | UnwindData |  |
| 519 | `InternalRegOpenClassKey` | `0xBD430` | 502 | UnwindData |  |
| 316 | `CoMarshalInterThreadInterfaceInStream` | `0xBE6F0` | 204 | UnwindData |  |
| 367 | `CreateStreamOnHGlobal` | `0xBE8C0` | 543 | UnwindData |  |
| 104 | *Ordinal Only* | `0xC1A40` | 101 | UnwindData |  |
| 102 | *Ordinal Only* | `0xC1B20` | 85 | UnwindData |  |
| 101 | *Ordinal Only* | `0xC1B80` | 85 | UnwindData |  |
| 82 | `RoFailFastWithErrorContextInternal2` | `0xC24B0` | 1,412 | UnwindData |  |
| 543 | `RoCaptureErrorContext` | `0xC2C30` | 490 | UnwindData |  |
| 291 | `CoGetErrorInfo` | `0xC2EC0` | 194 | UnwindData |  |
| 376 | `GetErrorInfo` | `0xC2EC0` | 194 | UnwindData |  |
| 90 | *Ordinal Only* | `0xC3150` | 337 | UnwindData |  |
| 157 | *Ordinal Only* | `0xC32B0` | 148 | UnwindData |  |
| 309 | `CoInitializeSecurity` | `0xC5680` | 2,894 | UnwindData |  |
| 307 | `CoIncrementMTAUsage` | `0xC94A0` | 139 | UnwindData |  |
| 297 | `CoGetModuleArchitecture` | `0xCB570` | 1,322 | UnwindData |  |
| 547 | `RoGetActivatableClassRegistration` | `0xD09A0` | 239 | UnwindData |  |
| 558 | `RoOriginateError` | `0xD0E00` | 262 | UnwindData |  |
| 594 | `WindowsDeleteStringBuffer` | `0xD3470` | 73 | UnwindData |  |
| 604 | `WindowsStringHasEmbeddedNull` | `0xD82E0` | 127 | UnwindData |  |
| 554 | `RoGetServerActivatableClasses` | `0xD8610` | 244 | UnwindData |  |
| 374 | `FreePropVariantArrayWorker` | `0xDC4C0` | 125 | UnwindData |  |
| 597 | `WindowsGetStringRawBuffer` | `0xE42A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `CoGetApartmentType` | `0xE42E0` | 57 | UnwindData |  |
| 537 | `NdrpFindInterface` | `0xE4580` | 50 | UnwindData |  |
| 470 | `IIDFromString` | `0xE7090` | 82 | UnwindData |  |
| 334 | `CoRegisterSurrogateEx` | `0xE7E20` | 621 | UnwindData |  |
| 276 | `CoFreeUnusedLibrariesEx` | `0xE8EC0` | 69 | UnwindData |  |
| 589 | `WindowsCompareStringOrdinal` | `0xEA250` | 18 | UnwindData |  |
| 371 | `DllGetClassObject` | `0xECA70` | 493 | UnwindData |  |
| 305 | `CoGetTreatAsClass` | `0xEF3D0` | 9,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `CoIsOle1Class` | `0xF1990` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `ProgIDFromCLSID` | `0xF1C90` | 439 | UnwindData |  |
| 154 | *Ordinal Only* | `0xF76D0` | 713 | UnwindData |  |
| 257 | `CoCopyProxy` | `0xF7A00` | 134 | UnwindData |  |
| 349 | `CoSetProxyBlanket` | `0xF7A90` | 297 | UnwindData |  |
| 295 | `CoGetMalloc` | `0xF7F50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `NdrExtStubInitialize` | `0xF7F80` | 114 | UnwindData |  |
| 314 | `CoLockObjectExternal` | `0xF8000` | 475 | UnwindData |  |
| 565 | `RoReportFailedDelegate` | `0xF8DD0` | 414 | UnwindData |  |
| 287 | `CoGetContextToken` | `0xFB430` | 178 | UnwindData |  |
| 395 | `HBITMAP_UserUnmarshal` | `0xFBDF0` | 136 | UnwindData |  |
| 201 | *Ordinal Only* | `0xFBF20` | 281 | UnwindData |  |
| 585 | `WdtpInterfacePointer_UserSize` | `0xFC040` | 157 | UnwindData |  |
| 417 | `HGLOBAL_UserSize` | `0xFC0F0` | 291 | UnwindData |  |
| 105 | `CLIPFORMAT_UserSize` | `0xFC540` | 297 | UnwindData |  |
| 203 | *Ordinal Only* | `0xFC670` | 136 | UnwindData |  |
| 588 | `WdtpInterfacePointer_UserUnmarshal64` | `0xFC700` | 123 | UnwindData |  |
| 204 | *Ordinal Only* | `0xFC860` | 187 | UnwindData |  |
| 107 | `CLIPFORMAT_UserUnmarshal` | `0xFCB20` | 475 | UnwindData |  |
| 587 | `WdtpInterfacePointer_UserUnmarshal` | `0xFCD10` | 120 | UnwindData |  |
| 221 | *Ordinal Only* | `0xFCD90` | 485 | UnwindData |  |
| 224 | *Ordinal Only* | `0xFCF80` | 186 | UnwindData |  |
| 223 | *Ordinal Only* | `0xFD280` | 136 | UnwindData |  |
| 396 | `HBITMAP_UserUnmarshal64` | `0xFD7D0` | 136 | UnwindData |  |
| 460 | `HSTRING_UserUnmarshal64` | `0xFDA90` | 584 | UnwindData |  |
| 418 | `HGLOBAL_UserSize64` | `0xFDE30` | 221 | UnwindData |  |
| 586 | `WdtpInterfacePointer_UserSize64` | `0xFDF20` | 204 | UnwindData |  |
| 106 | `CLIPFORMAT_UserSize64` | `0xFE030` | 291 | UnwindData |  |
| 108 | `CLIPFORMAT_UserUnmarshal64` | `0xFE160` | 602 | UnwindData |  |
| 394 | `HBITMAP_UserSize64` | `0xFE650` | 258 | UnwindData |  |
| 393 | `HBITMAP_UserSize` | `0xFE760` | 318 | UnwindData |  |
| 303 | `CoGetStdMarshalEx` | `0x101340` | 318 | UnwindData |  |
| 261 | `CoCreateInstance` | `0x103250` | 261 | UnwindData |  |
| 179 | *Ordinal Only* | `0x103550` | 245 | UnwindData |  |
| 555 | `RoInitialize` | `0x103650` | 163 | UnwindData |  |
| 342 | `CoRevokeDeviceCatalog` | `0x103F60` | 32 | UnwindData |  |
| 562 | `RoRegisterActivationFactories` | `0x105510` | 515 | UnwindData |  |
| 120 | *Ordinal Only* | `0x106570` | 386 | UnwindData |  |
| 296 | `CoGetMarshalSizeMax` | `0x106B90` | 511 | UnwindData |  |
| 529 | `InternalTlsAllocData` | `0x107BA0` | 96 | UnwindData |  |
| 166 | *Ordinal Only* | `0x108350` | 367 | UnwindData |  |
| 457 | `HSTRING_UserSize` | `0x1087F0` | 138 | UnwindData |  |
| 458 | `HSTRING_UserSize64` | `0x10B1F0` | 143 | UnwindData |  |
| 606 | `WindowsSubstringWithSpecifiedLength` | `0x10CE30` | 443 | UnwindData |  |
| 160 | *Ordinal Only* | `0x10D550` | 1,613 | UnwindData |  |
| 351 | `CoSwitchCallContext` | `0x10E880` | 101 | UnwindData |  |
| 354 | `CoTaskMemRealloc` | `0x10EE50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `PropVariantClear` | `0x10EE80` | 11,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | *Ordinal Only* | `0x111C70` | 36 | UnwindData |  |
| 283 | `CoGetCancelObject` | `0x1128B0` | 156 | UnwindData |  |
| 256 | `CoCancelCall` | `0x112960` | 204 | UnwindData |  |
| 132 | `CStdAsyncStubBuffer_Disconnect` | `0x112DF0` | 36 | UnwindData |  |
| 244 | `CStdStubBuffer_Disconnect` | `0x112DF0` | 36 | UnwindData |  |
| 117 | `CStdAsyncStubBuffer2_Disconnect` | `0x112E60` | 60 | UnwindData |  |
| 237 | `CStdStubBuffer2_Disconnect` | `0x112E60` | 60 | UnwindData |  |
| 180 | *Ordinal Only* | `0x113D70` | 158 | UnwindData |  |
| 238 | `CStdStubBuffer2_QueryInterface` | `0x114DD0` | 98 | UnwindData |  |
| 247 | `CStdStubBuffer_QueryInterface` | `0x114E40` | 249 | UnwindData |  |
| 177 | *Ordinal Only* | `0x115CD0` | 70 | UnwindData |  |
| 115 | `CLSIDFromString` | `0x115F40` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `HSTRING_UserFree` | `0x116AA0` | 32 | UnwindData |  |
| 454 | `HSTRING_UserFree64` | `0x116AA0` | 32 | UnwindData |  |
| 561 | `RoParameterizedTypeExtraGetTypeSignature` | `0x116AD0` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `CoRegisterMessageFilter` | `0x117270` | 441 | UnwindData |  |
| 178 | *Ordinal Only* | `0x1176F0` | 52 | UnwindData |  |
| 119 | `CStdAsyncStubBuffer_AddRef` | `0x118680` | 6,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `CStdStubBuffer_AddRef` | `0x118680` | 6,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `InternalCAggIdRelease` | `0x11A170` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | *Ordinal Only* | `0x11BDC0` | 7,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `CoRegisterInitializeSpy` | `0x11DA90` | 364 | UnwindData |  |
| 544 | `RoClearError` | `0x11DC80` | 87 | UnwindData |  |
| 181 | *Ordinal Only* | `0x11F540` | 135 | UnwindData |  |
| 378 | `GetHGlobalFromStream` | `0x122FC0` | 101 | UnwindData |  |
| 273 | `CoEnableCallCancellation` | `0x123380` | 79 | UnwindData |  |
| 270 | `CoDisableCallCancellation` | `0x1236D0` | 101 | UnwindData |  |
| 133 | *Ordinal Only* | `0x124F30` | 112 | UnwindData |  |
| 258 | `CoCreateErrorInfo` | `0x125BA0` | 165 | UnwindData |  |
| 366 | `CreateErrorInfo` | `0x125BA0` | 165 | UnwindData |  |
| 88 | *Ordinal Only* | `0x125C50` | 142 | UnwindData |  |
| 375 | `GetCatalogHelper` | `0x126910` | 118 | UnwindData |  |
| 343 | `CoRevokeInitializeSpy` | `0x127760` | 173 | UnwindData |  |
| 322 | `CoQueryProxyBlanket` | `0x127A00` | 307 | UnwindData |  |
| 254 | `CoAddRefServerProcess` | `0x128A30` | 29 | UnwindData |  |
| 377 | `GetFuncDescs` | `0x128A70` | 372 | UnwindData |  |
| 269 | `CoDecrementMTAUsage` | `0x129C90` | 116 | UnwindData |  |
| 505 | `InternalIrotGetObject3` | `0x12B6F0` | 59 | UnwindData |  |
| 370 | `DllGetActivationFactory` | `0x12C3A0` | 45 | UnwindData |  |
| 500 | `InternalGetWindowPropInterface2` | `0x12D7B0` | 323 | UnwindData |  |
| 523 | `InternalRevokeWindowPropInterface` | `0x12D900` | 261 | UnwindData |  |
| 231 | *Ordinal Only* | `0x12ED80` | 78 | UnwindData |  |
| 603 | `WindowsReplaceString` | `0x12F9D0` | 223 | UnwindData |  |
| 251 | `CleanupTlsOleState` | `0x131300` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | *Ordinal Only* | `0x1322D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `HSTRING_UserMarshal` | `0x132350` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `ReleaseFuncDescs` | `0x132880` | 114 | UnwindData |  |
| 300 | `CoGetPSClsid` | `0x133950` | 200 | UnwindData |  |
| 294 | `CoGetInterfaceAndReleaseStream` | `0x134380` | 234 | UnwindData |  |
| 570 | `RoTransformError` | `0x134B70` | 75 | UnwindData |  |
| 235 | `CStdStubBuffer2_Connect` | `0x1357F0` | 50 | UnwindData |  |
| 240 | `CStdStubBuffer_Connect` | `0x135830` | 95 | UnwindData |  |
| 274 | `CoFileTimeNow` | `0x136880` | 140 | UnwindData |  |
| 331 | `CoRegisterPSClsid` | `0x1386B0` | 63 | UnwindData |  |
| 373 | `FreePropVariantArray` | `0x138700` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `CoGetProcessIdentifier` | `0x138CD0` | 3,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `CoGetCallerTID` | `0x139B90` | 88 | UnwindData |  |
| 312 | `CoIsHandlerConnected` | `0x139C50` | 117 | UnwindData |  |
| 365 | `CoWaitForMultipleObjects` | `0x13A1B0` | 149 | UnwindData |  |
| 579 | `StringFromIID` | `0x13A9A0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `RoGetApartmentIdentifier` | `0x13AA90` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `WindowsSubstring` | `0x13AEE0` | 161 | UnwindData |  |
| 140 | *Ordinal Only* | `0x13AF90` | 132 | UnwindData |  |
| 250 | `CleanupTlsComl2State` | `0x13D350` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `HBITMAP_UserFree64` | `0x13DF80` | 85 | UnwindData |  |
| 552 | `RoGetMatchingRestrictedErrorInfo` | `0x13EF70` | 325 | UnwindData |  |
| 85 | `CLIPFORMAT_UserFree` | `0x140EC0` | 37 | UnwindData |  |
| 89 | `CLIPFORMAT_UserFree64` | `0x140EC0` | 37 | UnwindData |  |
| 69 | *Ordinal Only* | `0x141130` | 51 | UnwindData |  |
| 387 | `HACCEL_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `HACCEL_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `HBRUSH_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `HBRUSH_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `HDC_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `HDC_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `HICON_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `HICON_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `HMENU_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `HMENU_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `HMONITOR_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `HMONITOR_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `HRGN_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `HRGN_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `HWND_UserUnmarshal` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `HWND_UserUnmarshal64` | `0x141B90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `CLSIDFromOle1Class` | `0x142090` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `InternalIsApartmentInitialized` | `0x1422D0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | *Ordinal Only* | `0x1430F0` | 683 | UnwindData |  |
| 389 | `HBITMAP_UserFree` | `0x1436C0` | 87 | UnwindData |  |
| 271 | `CoDisconnectContext` | `0x143720` | 108 | UnwindData |  |
| 110 | *Ordinal Only* | `0x1437B0` | 82 | UnwindData |  |
| 385 | `HACCEL_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `HACCEL_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `HBRUSH_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `HBRUSH_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `HDC_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `HDC_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `HICON_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `HICON_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `HMENU_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `HMENU_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `HMONITOR_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `HMONITOR_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `HRGN_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `HRGN_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `HWND_UserSize` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `HWND_UserSize64` | `0x1439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `InternalCoIsSurrogateProcess` | `0x1439B0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `RoGetErrorReportingFlags` | `0x143C00` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `CoFreeUnusedLibraries` | `0x1441A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | *Ordinal Only* | `0x1441E0` | 36 | UnwindData |  |
| 290 | `CoGetDefaultContext` | `0x144EF0` | 299 | UnwindData |  |
| 242 | `CStdStubBuffer_DebugServerQueryInterface` | `0x145AD0` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `InternalIrotRevoke` | `0x1466E0` | 29 | UnwindData |  |
| 327 | `CoRegisterDeviceCatalog` | `0x148970` | 148 | UnwindData |  |
| 492 | `InternalCoUnregisterDisconnectCallback` | `0x14A620` | 133 | UnwindData |  |
| 383 | `HACCEL_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `HACCEL_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `HBRUSH_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `HBRUSH_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `HDC_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `HDC_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `HICON_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `HICON_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `HMENU_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `HMENU_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `HMONITOR_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `HMONITOR_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `HRGN_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `HRGN_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `HWND_UserMarshal` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `HWND_UserMarshal64` | `0x14AED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `CoGetCurrentProcess` | `0x14AF30` | 104 | UnwindData |  |
| 511 | `InternalIrotRegister` | `0x14BE90` | 58 | UnwindData |  |
| 368 | `DcomChannelSetHResult` | `0x14C0C0` | 4,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | *Ordinal Only* | `0x14D1B0` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `InternalIsProcessInitialized` | `0x14DB10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `RoTransformErrorW` | `0x14DB90` | 7,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `CoRegisterActivationFilter` | `0x14F880` | 105 | UnwindData |  |
| 574 | `SetCleanupFlag` | `0x14F8F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `CoMarshalHresult` | `0x14F9B0` | 74 | UnwindData |  |
| 490 | `InternalCoRegisterSurrogatedObject` | `0x151010` | 170 | UnwindData |  |
| 114 | `CLSIDFromProgIDEx` | `0x1510D0` | 145 | UnwindData |  |
| 355 | `CoTestCancel` | `0x1512A0` | 82 | UnwindData |  |
| 148 | *Ordinal Only* | `0x151520` | 55 | UnwindData |  |
| 333 | `CoRegisterSurrogate` | `0x1517C0` | 86 | UnwindData |  |
| 139 | *Ordinal Only* | `0x151A90` | 67 | UnwindData |  |
| 252 | `ClearCleanupFlag` | `0x151D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `RoSetErrorReportingFlags` | `0x151D50` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `InternalIrotNoteChangeTime` | `0x151F70` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `InternalIrotEnumRunning` | `0x1522C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `InternalIrotGetObject` | `0x1522C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `InternalIrotGetObject2` | `0x1522C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `InternalIrotGetTimeOfLastChange` | `0x1522C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `InternalIrotIsRunning` | `0x1522C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | *Ordinal Only* | `0x1522D0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `CoSuspendClassObjects` | `0x1526C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `InternalNotifyDDStartOrStop` | `0x1526E0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `InternalIrotIsRunning2` | `0x152A80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `RoRevokeActivationFactories` | `0x152AF0` | 104 | UnwindData |  |
| 165 | *Ordinal Only* | `0x152E90` | 387 | UnwindData |  |
| 489 | `InternalCoRegisterDisconnectCallback` | `0x1536E0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `CoGetCallState` | `0x1537D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `RoRegisterForApartmentShutdown` | `0x153810` | 5,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | *Ordinal Only* | `0x154E40` | 181 | UnwindData |  |
| 255 | `CoAllowUnmarshalerCLSID` | `0x155B50` | 184 | UnwindData |  |
| 234 | `CStdAsyncStubBuffer_Release` | `0x156330` | 86 | UnwindData |  |
| 359 | `CoUnmarshalHresult` | `0x1563E0` | 109 | UnwindData |  |
| 507 | `InternalIrotGetTimeOfLastChange2` | `0x156AD0` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `CStdAsyncStubBuffer_QueryInterface` | `0x157110` | 268 | UnwindData |  |
| 248 | `CleanupComl2StateInAllTls` | `0x158A40` | 114 | UnwindData |  |
| 249 | `CleanupOleStateInAllTls` | `0x158AC0` | 114 | UnwindData |  |
| 95 | *Ordinal Only* | `0x158B40` | 261 | UnwindData |  |
| 262 | `CoCreateInstanceEx` | `0x15D160` | 518 | UnwindData |  |
| 264 | `CoCreateInstanceFromApp` | `0x15D370` | 469 | UnwindData |  |
| 284 | `CoGetClassObject` | `0x15D550` | 393 | UnwindData |  |
| 325 | `CoRegisterClassObject` | `0x15D6E0` | 797 | UnwindData |  |
| 583 | `WdtpInterfacePointer_UserMarshal` | `0x161D30` | 257 | UnwindData |  |
| 584 | `WdtpInterfacePointer_UserMarshal64` | `0x161E40` | 257 | UnwindData |  |
| 91 | `CLIPFORMAT_UserMarshal` | `0x161F50` | 359 | UnwindData |  |
| 94 | `CLIPFORMAT_UserMarshal64` | `0x1620C0` | 388 | UnwindData |  |
| 391 | `HBITMAP_UserMarshal` | `0x162250` | 340 | UnwindData |  |
| 392 | `HBITMAP_UserMarshal64` | `0x1623B0` | 385 | UnwindData |  |
| 415 | `HGLOBAL_UserMarshal` | `0x162540` | 275 | UnwindData |  |
| 416 | `HGLOBAL_UserMarshal64` | `0x162660` | 276 | UnwindData |  |
| 202 | *Ordinal Only* | `0x162810` | 554 | UnwindData |  |
| 222 | *Ordinal Only* | `0x162A40` | 615 | UnwindData |  |
| 456 | `HSTRING_UserMarshal64` | `0x162E10` | 271 | UnwindData |  |
| 103 | *Ordinal Only* | `0x174240` | 116 | UnwindData |  |
| 608 | `WindowsTrimStringStart` | `0x175940` | 221 | UnwindData |  |
| 209 | *Ordinal Only* | `0x175CD0` | 442 | UnwindData |  |
| 121 | *Ordinal Only* | `0x1765B0` | 217 | UnwindData |  |
| 573 | `RoUnregisterForApartmentShutdown` | `0x1771A0` | 4,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `RoFailFastWithErrorContext` | `0x1781D0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `HDC_UserFree` | `0x178540` | 35,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `HRGN_UserFree` | `0x178540` | 35,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `InternalAppInvokeExceptionFilter` | `0x1810E0` | 27 | UnwindData |  |
| 473 | `InternalCAggIdSetHandler` | `0x181110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `InternalCCFreeUnused` | `0x181130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `InternalCMLSendReceive` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `InternalCanMakeOutCall` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `InternalCompleteObjRef` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `InternalFillLocalOXIDInfo` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `InternalGetWindowPropInterface` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `InternalMarshalObjRef` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `InternalRegisterWindowPropInterface` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `InternalReleaseMarshalObjRef` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `InternalStubInvoke` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `InternalUnmarshalObjRef` | `0x181140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `InternalCStdIdentityGetInternalUnk` | `0x181150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `InternalCStdIdentityUpdateFlags` | `0x181160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `InternalCallAsProxyExceptionFilter` | `0x181170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `InternalServerExceptionFilter` | `0x181170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `InternalCallFrameExceptionFilter` | `0x181180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `InternalCallerIsAppContainer` | `0x181190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `InternalCoStdMarshalObject` | `0x1811A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `InternalDoATClassCreate` | `0x1811B0` | 107 | UnwindData |  |
| 502 | `InternalIrotEnumRunning2` | `0x181230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `InternalOle1ClassFromCLSID2` | `0x181250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `InternalSTAInvoke` | `0x181260` | 36,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | *Ordinal Only* | `0x18A150` | 84 | UnwindData |  |
| 171 | *Ordinal Only* | `0x18A1B0` | 71 | UnwindData |  |
| 135 | *Ordinal Only* | `0x18A4B0` | 182 | UnwindData |  |
| 134 | *Ordinal Only* | `0x18A570` | 250 | UnwindData |  |
| 162 | *Ordinal Only* | `0x18A670` | 186 | UnwindData |  |
| 230 | *Ordinal Only* | `0x18A730` | 93 | UnwindData |  |
| 286 | `CoGetClassVersion` | `0x18AB80` | 232 | UnwindData |  |
| 70 | *Ordinal Only* | `0x18B000` | 146 | UnwindData |  |
| 310 | `CoInitializeWOW` | `0x18B0A0` | 123 | UnwindData |  |
| 71 | *Ordinal Only* | `0x18B130` | 296 | UnwindData |  |
| 329 | `CoRegisterMallocSpy` | `0x18B920` | 328 | UnwindData |  |
| 344 | `CoRevokeMallocSpy` | `0x18BA70` | 150 | UnwindData |  |
| 226 | *Ordinal Only* | `0x18BB10` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `EnableHookObject` | `0x18C130` | 76 | UnwindData |  |
| 379 | `GetHookInterface` | `0x18C190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `HkOleRegisterObject` | `0x18C1B0` | 34 | UnwindData |  |
| 356 | `CoTreatAsClass` | `0x18C900` | 6,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | *Ordinal Only* | `0x18E150` | 9,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `UpdateProcessTracing` | `0x190670` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `CoRegisterConsoleHandles` | `0x190810` | 241 | UnwindData |  |
| 332 | `CoRegisterRacActivationToken` | `0x190910` | 63 | UnwindData |  |
| 341 | `CoRevokeConsoleHandles` | `0x190960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `CoRevokeRacActivationToken` | `0x190980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `UpdateDCOMSettings` | `0x1909A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x1909B0` | 12,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | *Ordinal Only* | `0x1939A0` | 189 | UnwindData |  |
| 175 | *Ordinal Only* | `0x193A70` | 189 | UnwindData |  |
| 149 | *Ordinal Only* | `0x193B40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | *Ordinal Only* | `0x193B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x193B90` | 300 | UnwindData |  |
| 174 | *Ordinal Only* | `0x193CD0` | 287 | UnwindData |  |
| 346 | `CoSetCancelObject` | `0x1956C0` | 142 | UnwindData |  |
| 228 | *Ordinal Only* | `0x195760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | *Ordinal Only* | `0x195770` | 27 | UnwindData |  |
| 152 | *Ordinal Only* | `0x1957A0` | 4,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `CoQueryAuthenticationServices` | `0x196920` | 553 | UnwindData |  |
| 136 | *Ordinal Only* | `0x196BA0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `CoCreateObjectInContext` | `0x1976E0` | 276 | UnwindData |  |
| 267 | `CoDeactivateObject` | `0x197940` | 194 | UnwindData |  |
| 268 | `CoDecodeProxy` | `0x197A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `CoGetActivationState` | `0x197A40` | 47 | UnwindData |  |
| 304 | `CoGetSystemSecurityPermissions` | `0x197A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `CoInvalidateRemoteMachineBindings` | `0x197AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `CoReactivateObject` | `0x197AD0` | 176 | UnwindData |  |
| 338 | `CoRetireServer` | `0x197B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | *Ordinal Only* | `0x197BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | *Ordinal Only* | `0x197BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | *Ordinal Only* | `0x197BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | *Ordinal Only* | `0x197C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `CoSetOutgoingCallState` | `0x197C30` | 141 | UnwindData |  |
| 125 | *Ordinal Only* | `0x197CD0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | *Ordinal Only* | `0x197EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | *Ordinal Only* | `0x197EC0` | 293 | UnwindData |  |
| 163 | *Ordinal Only* | `0x1982E0` | 63 | UnwindData |  |
| 278 | `CoGetApartmentID` | `0x199660` | 96 | UnwindData |  |
| 138 | *Ordinal Only* | `0x19A040` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | *Ordinal Only* | `0x19A890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | *Ordinal Only* | `0x19A8A0` | 4,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | *Ordinal Only* | `0x19B980` | 62 | UnwindData |  |
| 98 | *Ordinal Only* | `0x19B9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `InternalCMLSendReceive2` | `0x19B9F0` | 224 | UnwindData |  |
| 487 | `InternalCanMakeOutCall2` | `0x19BAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `InternalOleModalLoopBlockFn` | `0x19BB00` | 59 | UnwindData |  |
| 526 | `InternalSetAptCallCtrlOnTlsIfRequired` | `0x19BB50` | 97 | UnwindData |  |
| 318 | `CoPopServiceDomain` | `0x19BC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `CoPushServiceDomain` | `0x19BC50` | 90 | UnwindData |  |
| 92 | *Ordinal Only* | `0x19CAF0` | 6,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | *Ordinal Only* | `0x19E380` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0x19EDB0` | 123 | UnwindData |  |
| 129 | *Ordinal Only* | `0x1A1750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | *Ordinal Only* | `0x1A1770` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | *Ordinal Only* | `0x1A1FC0` | 1,213 | UnwindData |  |
| 161 | *Ordinal Only* | `0x1A2600` | 38 | UnwindData |  |
| 369 | `DllDebugObjectRPCHook` | `0x1A3380` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `InternalCreateCAggId` | `0x1A3560` | 123 | UnwindData |  |
| 495 | `InternalCreateIdentityHandler` | `0x1A3D20` | 75 | UnwindData |  |
| 361 | `CoVrfCheckThreadState` | `0x1B8430` | 1,535 | UnwindData |  |
| 362 | `CoVrfGetThreadState` | `0x1B8A40` | 218 | UnwindData |  |
| 363 | `CoVrfReleaseThreadState` | `0x1B8B20` | 22 | UnwindData |  |
| 145 | *Ordinal Only* | `0x1B9250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | *Ordinal Only* | `0x1B9270` | 24,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `CoAddComDependencyOnPackage` | `0x1BF2F0` | 261 | UnwindData |  |
| 263 | `CoCreateInstanceExFromPackage` | `0x1BF400` | 161 | UnwindData |  |
| 265 | `CoCreateInstanceFromPackage` | `0x1BF4B0` | 245 | UnwindData |  |
| 285 | `CoGetClassObjectFromPackage` | `0x1BF5B0` | 577 | UnwindData |  |
| 227 | *Ordinal Only* | `0x1BF800` | 1,770 | UnwindData |  |
| 292 | `CoGetInstanceFromFile` | `0x1BFEF0` | 370 | UnwindData |  |
| 293 | `CoGetInstanceFromIStorage` | `0x1C0070` | 363 | UnwindData |  |
| 225 | *Ordinal Only* | `0x1C59E0` | 14,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `InternalCCGetClassInformationForDde` | `0x1C9180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `InternalCCGetClassInformationFromKey` | `0x1C91A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `InternalCCSetDdeServerWindow` | `0x1C91C0` | 116 | UnwindData |  |
| 581 | `WdtpInterfacePointer_UserFree` | `0x1CA630` | 27 | UnwindData |  |
| 582 | `WdtpInterfacePointer_UserFree64` | `0x1CA660` | 2,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | *Ordinal Only* | `0x1CB140` | 85 | UnwindData |  |
| 208 | *Ordinal Only* | `0x1CB140` | 85 | UnwindData |  |
| 186 | *Ordinal Only* | `0x1CB1A0` | 243 | UnwindData |  |
| 206 | *Ordinal Only* | `0x1CB2A0` | 295 | UnwindData |  |
| 185 | *Ordinal Only* | `0x1CB3D0` | 223 | UnwindData |  |
| 205 | *Ordinal Only* | `0x1CB4C0` | 268 | UnwindData |  |
| 187 | *Ordinal Only* | `0x1CB5E0` | 121 | UnwindData |  |
| 207 | *Ordinal Only* | `0x1CB660` | 121 | UnwindData |  |
| 192 | *Ordinal Only* | `0x1CB6E0` | 164 | UnwindData |  |
| 212 | *Ordinal Only* | `0x1CB6E0` | 164 | UnwindData |  |
| 190 | *Ordinal Only* | `0x1CB790` | 375 | UnwindData |  |
| 210 | *Ordinal Only* | `0x1CB910` | 507 | UnwindData |  |
| 189 | *Ordinal Only* | `0x1CBB20` | 393 | UnwindData |  |
| 191 | *Ordinal Only* | `0x1CBCB0` | 121 | UnwindData |  |
| 211 | *Ordinal Only* | `0x1CBD30` | 121 | UnwindData |  |
| 196 | *Ordinal Only* | `0x1CBDB0` | 85 | UnwindData |  |
| 216 | *Ordinal Only* | `0x1CBDB0` | 85 | UnwindData |  |
| 194 | *Ordinal Only* | `0x1CBE10` | 243 | UnwindData |  |
| 214 | *Ordinal Only* | `0x1CBF10` | 295 | UnwindData |  |
| 193 | *Ordinal Only* | `0x1CC040` | 223 | UnwindData |  |
| 213 | *Ordinal Only* | `0x1CC130` | 268 | UnwindData |  |
| 195 | *Ordinal Only* | `0x1CC250` | 339 | UnwindData |  |
| 215 | *Ordinal Only* | `0x1CC3B0` | 477 | UnwindData |  |
| 413 | `HGLOBAL_UserFree` | `0x1CC5D0` | 85 | UnwindData |  |
| 414 | `HGLOBAL_UserFree64` | `0x1CC5D0` | 85 | UnwindData |  |
| 419 | `HGLOBAL_UserUnmarshal` | `0x1CC630` | 129 | UnwindData |  |
| 420 | `HGLOBAL_UserUnmarshal64` | `0x1CC6C0` | 129 | UnwindData |  |
| 445 | `HPALETTE_UserFree` | `0x1CCBE0` | 85 | UnwindData |  |
| 446 | `HPALETTE_UserFree64` | `0x1CCBE0` | 85 | UnwindData |  |
| 447 | `HPALETTE_UserMarshal` | `0x1CCC40` | 269 | UnwindData |  |
| 448 | `HPALETTE_UserMarshal64` | `0x1CCD60` | 323 | UnwindData |  |
| 449 | `HPALETTE_UserSize` | `0x1CCEB0` | 237 | UnwindData |  |
| 450 | `HPALETTE_UserSize64` | `0x1CCFB0` | 232 | UnwindData |  |
| 451 | `HPALETTE_UserUnmarshal` | `0x1CD0A0` | 121 | UnwindData |  |
| 452 | `HPALETTE_UserUnmarshal64` | `0x1CD120` | 121 | UnwindData |  |
| 200 | *Ordinal Only* | `0x1CD250` | 84 | UnwindData |  |
| 220 | *Ordinal Only* | `0x1CD250` | 84 | UnwindData |  |
| 198 | *Ordinal Only* | `0x1CD2B0` | 232 | UnwindData |  |
| 218 | *Ordinal Only* | `0x1CD3A0` | 235 | UnwindData |  |
| 197 | *Ordinal Only* | `0x1CD4A0` | 270 | UnwindData |  |
| 217 | *Ordinal Only* | `0x1CD5C0` | 288 | UnwindData |  |
| 199 | *Ordinal Only* | `0x1CD6F0` | 765 | UnwindData |  |
| 219 | *Ordinal Only* | `0x1CDA00` | 789 | UnwindData |  |
| 298 | `CoGetModuleType` | `0x1CF210` | 219 | UnwindData |  |
| 229 | *Ordinal Only* | `0x1DAC90` | 110,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | *Ordinal Only* | `0x1F5AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | *Ordinal Only* | `0x1F5AC0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `WindowsInspectString` | `0x1F5CE0` | 94 | UnwindData |  |
| 599 | `WindowsInspectString2` | `0x1F5D50` | 77 | UnwindData |  |
| 83 | `RoFailFastWithErrorContextInternal` | `0x1F63A0` | 373 | UnwindData |  |
| 556 | `RoInspectCapturedStackBackTrace` | `0x1F65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `RoInspectThreadErrorInfo` | `0x1F65C0` | 159 | UnwindData |  |
| 564 | `RoReportCapabilityCheckFailure` | `0x1F6670` | 51 | UnwindData |  |
| 566 | `RoReportUnhandledError` | `0x1F66B0` | 42 | UnwindData |  |
| 567 | `RoResolveRestrictedErrorInfoReference` | `0x1F79E0` | 183 | UnwindData |  |
| 546 | `RoFreeParameterizedTypeExtra` | `0x1F8A50` | 38 | UnwindData |  |
| 116 | `CStdAsyncStubBuffer2_Connect` | `0x1F8C60` | 61 | UnwindData |  |
| 118 | `CStdAsyncStubBuffer2_Release` | `0x1F8CB0` | 107 | UnwindData |  |
| 131 | `CStdAsyncStubBuffer_Connect` | `0x1F8D30` | 69 | UnwindData |  |
| 144 | `CStdAsyncStubBuffer_Invoke` | `0x1F8D80` | 296 | UnwindData |  |
| 236 | `CStdStubBuffer2_CountRefs` | `0x1F8F90` | 47 | UnwindData |  |
| 241 | `CStdStubBuffer_CountRefs` | `0x1F9070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `CStdStubBuffer_IsIIDSupported` | `0x1F9090` | 73 | UnwindData |  |
| 536 | `NdrOleInitializeExtension` | `0x1F98E0` | 74 | UnwindData |  |
| 81 | *Ordinal Only* | `0x1FEE10` | 60 | UnwindData |  |
| 170 | *Ordinal Only* | `0x1FEE60` | 236 | UnwindData |  |
| 80 | *Ordinal Only* | `0x1FEF60` | 64 | UnwindData |  |
| 169 | *Ordinal Only* | `0x1FEFB0` | 307 | UnwindData |  |
| 79 | *Ordinal Only* | `0x20DB00` | 433 | UnwindData |  |
| 32 | `NdrProxyForwardingFunction3` | `0x220DB0` | 71 | UnwindData |  |
| 33 | `NdrProxyForwardingFunction4` | `0x220E00` | 71 | UnwindData |  |
| 34 | `NdrProxyForwardingFunction5` | `0x220E50` | 71 | UnwindData |  |
| 35 | `NdrProxyForwardingFunction6` | `0x220EA0` | 71 | UnwindData |  |
| 36 | `NdrProxyForwardingFunction7` | `0x220EF0` | 71 | UnwindData |  |
| 37 | `NdrProxyForwardingFunction8` | `0x220F40` | 71 | UnwindData |  |
| 38 | `NdrProxyForwardingFunction9` | `0x220F90` | 71 | UnwindData |  |
| 39 | `NdrProxyForwardingFunction10` | `0x220FE0` | 71 | UnwindData |  |
| 40 | `NdrProxyForwardingFunction11` | `0x221030` | 71 | UnwindData |  |
| 41 | `NdrProxyForwardingFunction12` | `0x221080` | 71 | UnwindData |  |
| 42 | `NdrProxyForwardingFunction13` | `0x2210D0` | 71 | UnwindData |  |
| 43 | `NdrProxyForwardingFunction14` | `0x221120` | 71 | UnwindData |  |
| 44 | `NdrProxyForwardingFunction15` | `0x221170` | 71 | UnwindData |  |
| 45 | `NdrProxyForwardingFunction16` | `0x2211C0` | 74 | UnwindData |  |
| 46 | `NdrProxyForwardingFunction17` | `0x221210` | 74 | UnwindData |  |
| 47 | `NdrProxyForwardingFunction18` | `0x221260` | 74 | UnwindData |  |
| 48 | `NdrProxyForwardingFunction19` | `0x2212B0` | 74 | UnwindData |  |
| 49 | `NdrProxyForwardingFunction20` | `0x221300` | 74 | UnwindData |  |
| 50 | `NdrProxyForwardingFunction21` | `0x221350` | 74 | UnwindData |  |
| 51 | `NdrProxyForwardingFunction22` | `0x2213A0` | 74 | UnwindData |  |
| 52 | `NdrProxyForwardingFunction23` | `0x2213F0` | 74 | UnwindData |  |
| 53 | `NdrProxyForwardingFunction24` | `0x221440` | 74 | UnwindData |  |
| 54 | `NdrProxyForwardingFunction25` | `0x221490` | 74 | UnwindData |  |
| 55 | `NdrProxyForwardingFunction26` | `0x2214E0` | 74 | UnwindData |  |
| 56 | `NdrProxyForwardingFunction27` | `0x221530` | 74 | UnwindData |  |
| 57 | `NdrProxyForwardingFunction28` | `0x221580` | 74 | UnwindData |  |
| 58 | `NdrProxyForwardingFunction29` | `0x2215D0` | 74 | UnwindData |  |
| 59 | `NdrProxyForwardingFunction30` | `0x221620` | 74 | UnwindData |  |
| 60 | `NdrProxyForwardingFunction31` | `0x221670` | 74 | UnwindData |  |
| 61 | `NdrProxyForwardingFunction32` | `0x2216C0` | 74 | UnwindData |  |
| 2 | `ObjectStublessClient3` | `0x248CD0` | 10 | UnwindData |  |
| 3 | `ObjectStublessClient4` | `0x248CE0` | 10 | UnwindData |  |
| 4 | `ObjectStublessClient5` | `0x248CF0` | 10 | UnwindData |  |
| 5 | `ObjectStublessClient6` | `0x248D00` | 10 | UnwindData |  |
| 6 | `ObjectStublessClient7` | `0x248D10` | 10 | UnwindData |  |
| 7 | `ObjectStublessClient8` | `0x248D20` | 10 | UnwindData |  |
| 8 | `ObjectStublessClient9` | `0x248D30` | 10 | UnwindData |  |
| 9 | `ObjectStublessClient10` | `0x248D40` | 10 | UnwindData |  |
| 10 | `ObjectStublessClient11` | `0x248D50` | 10 | UnwindData |  |
| 11 | `ObjectStublessClient12` | `0x248D60` | 10 | UnwindData |  |
| 12 | `ObjectStublessClient13` | `0x248D70` | 10 | UnwindData |  |
| 13 | `ObjectStublessClient14` | `0x248D80` | 10 | UnwindData |  |
| 14 | `ObjectStublessClient15` | `0x248D90` | 10 | UnwindData |  |
| 15 | `ObjectStublessClient16` | `0x248DA0` | 10 | UnwindData |  |
| 16 | `ObjectStublessClient17` | `0x248DB0` | 10 | UnwindData |  |
| 17 | `ObjectStublessClient18` | `0x248DC0` | 10 | UnwindData |  |
| 18 | `ObjectStublessClient19` | `0x248DD0` | 10 | UnwindData |  |
| 19 | `ObjectStublessClient20` | `0x248DE0` | 10 | UnwindData |  |
| 20 | `ObjectStublessClient21` | `0x248DF0` | 10 | UnwindData |  |
| 21 | `ObjectStublessClient22` | `0x248E00` | 10 | UnwindData |  |
| 22 | `ObjectStublessClient23` | `0x248E10` | 10 | UnwindData |  |
| 23 | `ObjectStublessClient24` | `0x248E20` | 10 | UnwindData |  |
| 24 | `ObjectStublessClient25` | `0x248E30` | 10 | UnwindData |  |
| 25 | `ObjectStublessClient26` | `0x248E40` | 10 | UnwindData |  |
| 26 | `ObjectStublessClient27` | `0x248E50` | 10 | UnwindData |  |
| 27 | `ObjectStublessClient28` | `0x248E60` | 10 | UnwindData |  |
| 28 | `ObjectStublessClient29` | `0x248E70` | 10 | UnwindData |  |
| 29 | `ObjectStublessClient30` | `0x248E80` | 10 | UnwindData |  |
| 30 | `ObjectStublessClient31` | `0x248E90` | 10 | UnwindData |  |
| 31 | `ObjectStublessClient32` | `0x248EA0` | 10 | UnwindData |  |
| 183 | *Ordinal Only* | `0x2D7F30` | 0 | Indeterminate |  |
