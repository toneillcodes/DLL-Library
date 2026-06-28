# Binary Specification: combase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\combase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93c0850327562f90eff88dcc9919a33720531653d35c9971eeb5fed18ba34381`
* **Total Exported Functions:** 608

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 336 | `CoReleaseServerProcess` | `0x5ED0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | *Ordinal Only* | `0x7610` | 13,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0xA900` | 181 | UnwindData |  |
| 340 | `CoRevokeClassObject` | `0xADC0` | 65 | UnwindData |  |
| 272 | `CoDisconnectObject` | `0xB0A0` | 605 | UnwindData |  |
| 337 | `CoResumeClassObjects` | `0xB5D0` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `CoFreeUnusedLibrariesEx` | `0xBC30` | 108 | UnwindData |  |
| 334 | `CoRegisterSurrogateEx` | `0xD3C0` | 621 | UnwindData |  |
| 271 | `CoDisconnectContext` | `0xE2A0` | 110 | UnwindData |  |
| 316 | `CoMarshalInterThreadInterfaceInStream` | `0xE9A0` | 204 | UnwindData |  |
| 367 | `CreateStreamOnHGlobal` | `0xEB70` | 543 | UnwindData |  |
| 577 | `StringFromCLSID` | `0x11B90` | 436 | UnwindData |  |
| 364 | `CoWaitForMultipleHandles` | `0x16270` | 253 | UnwindData |  |
| 352 | `CoTaskMemAlloc` | `0x19C10` | 78 | UnwindData |  |
| 317 | `CoMarshalInterface` | `0x252B0` | 1,770 | UnwindData |  |
| 360 | `CoUnmarshalInterface` | `0x25B20` | 2,042 | UnwindData |  |
| 243 | `CStdStubBuffer_DebugServerRelease` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `HACCEL_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `HACCEL_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `HBRUSH_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `HBRUSH_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `HDC_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `HICON_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `HICON_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `HMENU_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `HMENU_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `HMONITOR_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `HMONITOR_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `HRGN_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `HWND_UserFree` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `HWND_UserFree64` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `InternalFreeObjRef` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `InternalSetOleThunkWowPtr` | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | *Ordinal Only* | `0x2F970` | 25,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `CoReleaseMarshalData` | `0x35DE0` | 587 | UnwindData |  |
| 288 | `CoGetCurrentLogicalThreadId` | `0x3CBC0` | 65 | UnwindData |  |
| 480 | `InternalCStdIdentityGetIProxyManager` | `0x3E740` | 6,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `RoGetAgileReference` | `0x401B0` | 1,780 | UnwindData |  |
| 260 | `CoCreateGuid` | `0x459D0` | 100 | UnwindData |  |
| 164 | *Ordinal Only* | `0x461F0` | 502 | UnwindData |  |
| 65 | *Ordinal Only* | `0x4DEA0` | 683 | UnwindData |  |
| 159 | *Ordinal Only* | `0x4E480` | 769 | UnwindData |  |
| 607 | `WindowsTrimStringEnd` | `0x509D0` | 278 | UnwindData |  |
| 600 | `WindowsIsStringEmpty` | `0x51EC0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `WindowsCreateStringReference` | `0x52540` | 317 | UnwindData |  |
| 593 | `WindowsDeleteString` | `0x56E80` | 93 | UnwindData |  |
| 259 | `CoCreateFreeThreadedMarshaler` | `0x5ADC0` | 25 | UnwindData |  |
| 153 | *Ordinal Only* | `0x5BAC0` | 881 | UnwindData |  |
| 459 | `HSTRING_UserUnmarshal` | `0x5C5D0` | 587 | UnwindData |  |
| 601 | `WindowsPreallocateStringBuffer` | `0x5D700` | 302 | UnwindData |  |
| 595 | `WindowsDuplicateString` | `0x5D840` | 103 | UnwindData |  |
| 591 | `WindowsCreateString` | `0x5DE10` | 75 | UnwindData |  |
| 559 | `RoOriginateErrorW` | `0x5E2D0` | 365 | UnwindData |  |
| 548 | `RoGetActivationFactory` | `0x60300` | 295 | UnwindData |  |
| 113 | `CLSIDFromProgID` | `0x62D40` | 430 | UnwindData |  |
| 542 | `RoActivateInstance` | `0x64090` | 412 | UnwindData |  |
| 321 | `CoQueryClientBlanket` | `0x6D520` | 171 | UnwindData |  |
| 168 | *Ordinal Only* | `0x6D8D0` | 231 | UnwindData |  |
| 184 | *Ordinal Only* | `0x6D9C0` | 562 | UnwindData |  |
| 167 | *Ordinal Only* | `0x6DDC0` | 384 | UnwindData |  |
| 306 | `CoImpersonateClient` | `0x6DF50` | 1,142 | UnwindData |  |
| 339 | `CoRevertToSelf` | `0x6E3D0` | 1,116 | UnwindData |  |
| 280 | `CoGetCallContext` | `0x6E840` | 752 | UnwindData |  |
| 302 | `CoGetStandardMarshal` | `0x6FAD0` | 1,248 | UnwindData |  |
| 299 | `CoGetObjectContext` | `0x710F0` | 100 | UnwindData |  |
| 296 | `CoGetMarshalSizeMax` | `0x71200` | 511 | UnwindData |  |
| 245 | `CStdStubBuffer_Invoke` | `0x81E10` | 428 | UnwindData |  |
| 90 | *Ordinal Only* | `0x854E0` | 337 | UnwindData |  |
| 157 | *Ordinal Only* | `0x85640` | 148 | UnwindData |  |
| 500 | `InternalGetWindowPropInterface2` | `0x86B80` | 323 | UnwindData |  |
| 521 | `InternalRegisterWindowPropInterface2` | `0x87020` | 412 | UnwindData |  |
| 523 | `InternalRevokeWindowPropInterface` | `0x872D0` | 261 | UnwindData |  |
| 309 | `CoInitializeSecurity` | `0x8AA50` | 2,894 | UnwindData |  |
| 576 | `SetRestrictedErrorInfo` | `0x8E880` | 152 | UnwindData |  |
| 176 | *Ordinal Only* | `0x8E920` | 269 | UnwindData |  |
| 380 | `GetRestrictedErrorInfo` | `0x8EA40` | 268 | UnwindData |  |
| 347 | `CoSetErrorInfo` | `0x8F280` | 310 | UnwindData |  |
| 575 | `SetErrorInfo` | `0x8F280` | 310 | UnwindData |  |
| 555 | `RoInitialize` | `0x99910` | 163 | UnwindData |  |
| 261 | `CoCreateInstance` | `0x9A770` | 919 | UnwindData |  |
| 262 | `CoCreateInstanceEx` | `0x9AB10` | 846 | UnwindData |  |
| 572 | `RoUninitialize` | `0x9BFD0` | 15 | UnwindData |  |
| 357 | `CoUninitialize` | `0x9BFF0` | 755 | UnwindData |  |
| 308 | `CoInitializeEx` | `0x9C310` | 336 | UnwindData |  |
| 532 | `NdrCStdStubBuffer2_Release` | `0x9DD50` | 217 | UnwindData |  |
| 533 | `NdrCStdStubBuffer_Release` | `0x9DD50` | 217 | UnwindData |  |
| 353 | `CoTaskMemFree` | `0x9E9C0` | 83 | UnwindData |  |
| 87 | *Ordinal Only* | `0xA54E0` | 353 | UnwindData |  |
| 358 | `CoUnloadingWOW` | `0xA8940` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | *Ordinal Only* | `0xA9BB0` | 126 | UnwindData |  |
| 305 | `CoGetTreatAsClass` | `0xAF350` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `CoIsOle1Class` | `0xAF5B0` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `ProgIDFromCLSID` | `0xAFA20` | 487 | UnwindData |  |
| 519 | `InternalRegOpenClassKey` | `0xB06B0` | 502 | UnwindData |  |
| 578 | `StringFromGUID2` | `0xB2EE0` | 33 | UnwindData |  |
| 297 | `CoGetModuleArchitecture` | `0xC0200` | 1,322 | UnwindData |  |
| 547 | `RoGetActivatableClassRegistration` | `0xC5630` | 239 | UnwindData |  |
| 558 | `RoOriginateError` | `0xC5A90` | 262 | UnwindData |  |
| 594 | `WindowsDeleteStringBuffer` | `0xC8130` | 73 | UnwindData |  |
| 560 | `RoOriginateLanguageException` | `0xC82B0` | 126 | UnwindData |  |
| 596 | `WindowsGetStringLen` | `0xC9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `WindowsPromoteStringBuffer` | `0xC9D60` | 127 | UnwindData |  |
| 553 | `RoGetParameterizedTypeInstanceIID` | `0xCFAB0` | 392 | UnwindData |  |
| 590 | `WindowsConcatString` | `0xD0D80` | 479 | UnwindData |  |
| 535 | `NdrOleDllGetClassObject` | `0xD65D0` | 121 | UnwindData |  |
| 377 | `GetFuncDescs` | `0xD8630` | 372 | UnwindData |  |
| 541 | `ReleaseFuncDescs` | `0xD87B0` | 114 | UnwindData |  |
| 604 | `WindowsStringHasEmbeddedNull` | `0xDBDA0` | 127 | UnwindData |  |
| 554 | `RoGetServerActivatableClasses` | `0xDBEB0` | 244 | UnwindData |  |
| 374 | `FreePropVariantArrayWorker` | `0xDD7C0` | 125 | UnwindData |  |
| 597 | `WindowsGetStringRawBuffer` | `0xE56F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `CoGetApartmentType` | `0xE5730` | 50 | UnwindData |  |
| 537 | `NdrpFindInterface` | `0xE59E0` | 50 | UnwindData |  |
| 314 | `CoLockObjectExternal` | `0xE5D40` | 544 | UnwindData |  |
| 470 | `IIDFromString` | `0xE9620` | 82 | UnwindData |  |
| 540 | `PropVariantCopy` | `0xEA7E0` | 12 | UnwindData |  |
| 589 | `WindowsCompareStringOrdinal` | `0xEAFB0` | 18 | UnwindData |  |
| 104 | *Ordinal Only* | `0xEFB50` | 101 | UnwindData |  |
| 102 | *Ordinal Only* | `0xEFC30` | 35 | UnwindData |  |
| 101 | *Ordinal Only* | `0xEFC60` | 35 | UnwindData |  |
| 82 | `RoFailFastWithErrorContextInternal2` | `0xF0310` | 1,412 | UnwindData |  |
| 543 | `RoCaptureErrorContext` | `0xF0A90` | 490 | UnwindData |  |
| 291 | `CoGetErrorInfo` | `0xF0D20` | 251 | UnwindData |  |
| 376 | `GetErrorInfo` | `0xF0D20` | 251 | UnwindData |  |
| 371 | `DllGetClassObject` | `0xF1A40` | 493 | UnwindData |  |
| 303 | `CoGetStdMarshalEx` | `0xF7060` | 318 | UnwindData |  |
| 283 | `CoGetCancelObject` | `0xF9470` | 156 | UnwindData |  |
| 256 | `CoCancelCall` | `0xF9520` | 204 | UnwindData |  |
| 154 | *Ordinal Only* | `0xFC710` | 753 | UnwindData |  |
| 257 | `CoCopyProxy` | `0xFCA70` | 134 | UnwindData |  |
| 349 | `CoSetProxyBlanket` | `0xFCB00` | 297 | UnwindData |  |
| 295 | `CoGetMalloc` | `0xFD020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `NdrExtStubInitialize` | `0xFD050` | 114 | UnwindData |  |
| 287 | `CoGetContextToken` | `0xFD990` | 203 | UnwindData |  |
| 395 | `HBITMAP_UserUnmarshal` | `0xFFDF0` | 136 | UnwindData |  |
| 201 | *Ordinal Only* | `0xFFF20` | 281 | UnwindData |  |
| 585 | `WdtpInterfacePointer_UserSize` | `0x100040` | 157 | UnwindData |  |
| 417 | `HGLOBAL_UserSize` | `0x1000F0` | 291 | UnwindData |  |
| 105 | `CLIPFORMAT_UserSize` | `0x100540` | 297 | UnwindData |  |
| 203 | *Ordinal Only* | `0x100670` | 136 | UnwindData |  |
| 588 | `WdtpInterfacePointer_UserUnmarshal64` | `0x100700` | 123 | UnwindData |  |
| 204 | *Ordinal Only* | `0x100860` | 187 | UnwindData |  |
| 107 | `CLIPFORMAT_UserUnmarshal` | `0x100B20` | 475 | UnwindData |  |
| 587 | `WdtpInterfacePointer_UserUnmarshal` | `0x100D10` | 120 | UnwindData |  |
| 221 | *Ordinal Only* | `0x100D90` | 485 | UnwindData |  |
| 224 | *Ordinal Only* | `0x100F80` | 186 | UnwindData |  |
| 223 | *Ordinal Only* | `0x101280` | 136 | UnwindData |  |
| 396 | `HBITMAP_UserUnmarshal64` | `0x1017D0` | 136 | UnwindData |  |
| 460 | `HSTRING_UserUnmarshal64` | `0x101A90` | 584 | UnwindData |  |
| 418 | `HGLOBAL_UserSize64` | `0x101E30` | 221 | UnwindData |  |
| 586 | `WdtpInterfacePointer_UserSize64` | `0x101F20` | 204 | UnwindData |  |
| 106 | `CLIPFORMAT_UserSize64` | `0x102030` | 291 | UnwindData |  |
| 108 | `CLIPFORMAT_UserUnmarshal64` | `0x102160` | 602 | UnwindData |  |
| 394 | `HBITMAP_UserSize64` | `0x102650` | 258 | UnwindData |  |
| 393 | `HBITMAP_UserSize` | `0x102760` | 318 | UnwindData |  |
| 565 | `RoReportFailedDelegate` | `0x103860` | 414 | UnwindData |  |
| 342 | `CoRevokeDeviceCatalog` | `0x1076B0` | 32 | UnwindData |  |
| 562 | `RoRegisterActivationFactories` | `0x108F00` | 515 | UnwindData |  |
| 120 | *Ordinal Only* | `0x1095D0` | 425 | UnwindData |  |
| 122 | *Ordinal Only* | `0x109780` | 73 | UnwindData |  |
| 529 | `InternalTlsAllocData` | `0x10B190` | 96 | UnwindData |  |
| 166 | *Ordinal Only* | `0x10BAB0` | 399 | UnwindData |  |
| 457 | `HSTRING_UserSize` | `0x10BF70` | 138 | UnwindData |  |
| 458 | `HSTRING_UserSize64` | `0x10D570` | 143 | UnwindData |  |
| 351 | `CoSwitchCallContext` | `0x10F480` | 149 | UnwindData |  |
| 606 | `WindowsSubstringWithSpecifiedLength` | `0x1102A0` | 443 | UnwindData |  |
| 160 | *Ordinal Only* | `0x1109C0` | 1,613 | UnwindData |  |
| 354 | `CoTaskMemRealloc` | `0x111E00` | 5,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `PropVariantClear` | `0x113450` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | *Ordinal Only* | `0x113CB0` | 53 | UnwindData |  |
| 95 | *Ordinal Only* | `0x114C90` | 175 | UnwindData |  |
| 307 | `CoIncrementMTAUsage` | `0x1154A0` | 139 | UnwindData |  |
| 67 | *Ordinal Only* | `0x115F20` | 36 | UnwindData |  |
| 132 | `CStdAsyncStubBuffer_Disconnect` | `0x116B80` | 36 | UnwindData |  |
| 244 | `CStdStubBuffer_Disconnect` | `0x116B80` | 36 | UnwindData |  |
| 117 | `CStdAsyncStubBuffer2_Disconnect` | `0x116C70` | 60 | UnwindData |  |
| 237 | `CStdStubBuffer2_Disconnect` | `0x116C70` | 60 | UnwindData |  |
| 180 | *Ordinal Only* | `0x1178D0` | 158 | UnwindData |  |
| 177 | *Ordinal Only* | `0x117A90` | 114 | UnwindData |  |
| 238 | `CStdStubBuffer2_QueryInterface` | `0x118970` | 98 | UnwindData |  |
| 247 | `CStdStubBuffer_QueryInterface` | `0x1189E0` | 249 | UnwindData |  |
| 115 | `CLSIDFromString` | `0x11A480` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `HSTRING_UserFree` | `0x11B420` | 32 | UnwindData |  |
| 454 | `HSTRING_UserFree64` | `0x11B420` | 32 | UnwindData |  |
| 561 | `RoParameterizedTypeExtraGetTypeSignature` | `0x11B450` | 2,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `CoRegisterMessageFilter` | `0x11BC30` | 441 | UnwindData |  |
| 119 | `CStdAsyncStubBuffer_AddRef` | `0x11D050` | 6,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `CStdStubBuffer_AddRef` | `0x11D050` | 6,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `InternalCAggIdRelease` | `0x11EA20` | 5,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | *Ordinal Only* | `0x11FDE0` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | *Ordinal Only* | `0x120880` | 2,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `CoRegisterInitializeSpy` | `0x121430` | 423 | UnwindData |  |
| 531 | `IsErrorPropagationEnabled` | `0x121B90` | 36 | UnwindData |  |
| 544 | `RoClearError` | `0x1226F0` | 87 | UnwindData |  |
| 181 | *Ordinal Only* | `0x124A80` | 135 | UnwindData |  |
| 273 | `CoEnableCallCancellation` | `0x127C80` | 125 | UnwindData |  |
| 270 | `CoDisableCallCancellation` | `0x129070` | 145 | UnwindData |  |
| 378 | `GetHGlobalFromStream` | `0x12A040` | 101 | UnwindData |  |
| 249 | `CleanupOleStateInAllTls` | `0x12AED0` | 91 | UnwindData |  |
| 251 | `CleanupTlsOleState` | `0x12AF40` | 5,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `CoCreateErrorInfo` | `0x12C4D0` | 165 | UnwindData |  |
| 366 | `CreateErrorInfo` | `0x12C4D0` | 165 | UnwindData |  |
| 86 | *Ordinal Only* | `0x12CD00` | 170 | UnwindData |  |
| 375 | `GetCatalogHelper` | `0x12D230` | 118 | UnwindData |  |
| 343 | `CoRevokeInitializeSpy` | `0x12D2B0` | 229 | UnwindData |  |
| 133 | *Ordinal Only* | `0x12DE80` | 84 | UnwindData |  |
| 322 | `CoQueryProxyBlanket` | `0x12E6E0` | 307 | UnwindData |  |
| 254 | `CoAddRefServerProcess` | `0x12F510` | 29 | UnwindData |  |
| 269 | `CoDecrementMTAUsage` | `0x130280` | 116 | UnwindData |  |
| 505 | `InternalIrotGetObject3` | `0x132400` | 59 | UnwindData |  |
| 370 | `DllGetActivationFactory` | `0x1334E0` | 45 | UnwindData |  |
| 231 | *Ordinal Only* | `0x1355A0` | 78 | UnwindData |  |
| 603 | `WindowsReplaceString` | `0x136180` | 223 | UnwindData |  |
| 93 | *Ordinal Only* | `0x138EC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `HSTRING_UserMarshal` | `0x138F40` | 5,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `CoGetPSClsid` | `0x13A5A0` | 200 | UnwindData |  |
| 294 | `CoGetInterfaceAndReleaseStream` | `0x13B230` | 234 | UnwindData |  |
| 570 | `RoTransformError` | `0x13BB00` | 75 | UnwindData |  |
| 235 | `CStdStubBuffer2_Connect` | `0x13C250` | 50 | UnwindData |  |
| 240 | `CStdStubBuffer_Connect` | `0x13C290` | 95 | UnwindData |  |
| 274 | `CoFileTimeNow` | `0x13D2E0` | 140 | UnwindData |  |
| 331 | `CoRegisterPSClsid` | `0x13EAC0` | 63 | UnwindData |  |
| 373 | `FreePropVariantArray` | `0x13EB10` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `CoGetProcessIdentifier` | `0x13F120` | 3,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `CoIsHandlerConnected` | `0x13FFC0` | 117 | UnwindData |  |
| 365 | `CoWaitForMultipleObjects` | `0x140690` | 149 | UnwindData |  |
| 248 | `CleanupComl2StateInAllTls` | `0x141FE0` | 89 | UnwindData |  |
| 250 | `CleanupTlsComl2State` | `0x142040` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `StringFromIID` | `0x1421C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `RoGetApartmentIdentifier` | `0x142250` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `WindowsSubstring` | `0x1426A0` | 161 | UnwindData |  |
| 140 | *Ordinal Only* | `0x142750` | 132 | UnwindData |  |
| 390 | `HBITMAP_UserFree64` | `0x144A50` | 85 | UnwindData |  |
| 552 | `RoGetMatchingRestrictedErrorInfo` | `0x1457D0` | 325 | UnwindData |  |
| 85 | `CLIPFORMAT_UserFree` | `0x147170` | 37 | UnwindData |  |
| 89 | `CLIPFORMAT_UserFree64` | `0x147170` | 37 | UnwindData |  |
| 69 | *Ordinal Only* | `0x1473E0` | 51 | UnwindData |  |
| 387 | `HACCEL_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `HACCEL_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `HBRUSH_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `HBRUSH_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `HDC_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `HDC_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `HICON_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `HICON_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `HMENU_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `HMENU_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `HMONITOR_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `HMONITOR_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `HRGN_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `HRGN_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `HWND_UserUnmarshal` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `HWND_UserUnmarshal64` | `0x147E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `CLSIDFromOle1Class` | `0x148360` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `InternalIsApartmentInitialized` | `0x148470` | 4,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `HBITMAP_UserFree` | `0x149710` | 87 | UnwindData |  |
| 282 | `CoGetCallerTID` | `0x149770` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `HACCEL_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `HACCEL_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `HBRUSH_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `HBRUSH_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `HDC_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `HDC_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `HICON_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `HICON_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `HMENU_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `HMENU_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `HMONITOR_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `HMONITOR_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `HRGN_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `HRGN_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `HWND_UserSize` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `HWND_UserSize64` | `0x149850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `InternalCoIsSurrogateProcess` | `0x149860` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `RoGetErrorReportingFlags` | `0x149C80` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `CoFreeUnusedLibraries` | `0x14A060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | *Ordinal Only* | `0x14A0A0` | 36 | UnwindData |  |
| 110 | *Ordinal Only* | `0x14A1A0` | 62 | UnwindData |  |
| 290 | `CoGetDefaultContext` | `0x14AD80` | 302 | UnwindData |  |
| 179 | *Ordinal Only* | `0x14B690` | 231 | UnwindData |  |
| 242 | `CStdStubBuffer_DebugServerQueryInterface` | `0x14B9E0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `InternalIrotRevoke` | `0x14C5E0` | 29 | UnwindData |  |
| 327 | `CoRegisterDeviceCatalog` | `0x14EE40` | 148 | UnwindData |  |
| 492 | `InternalCoUnregisterDisconnectCallback` | `0x1504C0` | 133 | UnwindData |  |
| 289 | `CoGetCurrentProcess` | `0x150D50` | 138 | UnwindData |  |
| 383 | `HACCEL_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `HACCEL_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `HBRUSH_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `HBRUSH_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `HDC_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `HDC_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `HICON_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `HICON_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `HMENU_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `HMENU_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `HMONITOR_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `HMONITOR_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `HRGN_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `HRGN_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `HWND_UserMarshal` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `HWND_UserMarshal64` | `0x150F30` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `InternalIrotRegister` | `0x151DB0` | 58 | UnwindData |  |
| 368 | `DcomChannelSetHResult` | `0x151FE0` | 4,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | *Ordinal Only* | `0x153000` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `InternalIsProcessInitialized` | `0x153AA0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `RoTransformErrorW` | `0x153B20` | 5,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `CoRegisterActivationFilter` | `0x155120` | 105 | UnwindData |  |
| 574 | `SetCleanupFlag` | `0x155190` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `CoMarshalHresult` | `0x155250` | 74 | UnwindData |  |
| 490 | `InternalCoRegisterSurrogatedObject` | `0x1567E0` | 170 | UnwindData |  |
| 114 | `CLSIDFromProgIDEx` | `0x1568A0` | 145 | UnwindData |  |
| 355 | `CoTestCancel` | `0x156A70` | 82 | UnwindData |  |
| 148 | *Ordinal Only* | `0x156DC0` | 55 | UnwindData |  |
| 333 | `CoRegisterSurrogate` | `0x156FB0` | 86 | UnwindData |  |
| 139 | *Ordinal Only* | `0x157280` | 67 | UnwindData |  |
| 252 | `ClearCleanupFlag` | `0x157520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `RoSetErrorReportingFlags` | `0x157540` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `InternalIrotNoteChangeTime` | `0x157760` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `InternalIrotEnumRunning` | `0x157BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `InternalIrotGetObject` | `0x157BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `InternalIrotGetObject2` | `0x157BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `InternalIrotGetTimeOfLastChange` | `0x157BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `InternalIrotIsRunning` | `0x157BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | *Ordinal Only* | `0x157BF0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `CoSuspendClassObjects` | `0x1581C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `InternalNotifyDDStartOrStop` | `0x1581E0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `InternalIrotIsRunning2` | `0x158580` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `RoRevokeActivationFactories` | `0x1585F0` | 104 | UnwindData |  |
| 165 | *Ordinal Only* | `0x158A90` | 378 | UnwindData |  |
| 489 | `InternalCoRegisterDisconnectCallback` | `0x1591D0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `CoGetCallState` | `0x1592C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `RoRegisterForApartmentShutdown` | `0x159300` | 5,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | *Ordinal Only* | `0x15A760` | 181 | UnwindData |  |
| 255 | `CoAllowUnmarshalerCLSID` | `0x15B380` | 184 | UnwindData |  |
| 234 | `CStdAsyncStubBuffer_Release` | `0x15BB50` | 86 | UnwindData |  |
| 359 | `CoUnmarshalHresult` | `0x15BC00` | 109 | UnwindData |  |
| 507 | `InternalIrotGetTimeOfLastChange2` | `0x15C270` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `CStdAsyncStubBuffer_QueryInterface` | `0x15C8B0` | 268 | UnwindData |  |
| 264 | `CoCreateInstanceFromApp` | `0x160FC0` | 516 | UnwindData |  |
| 284 | `CoGetClassObject` | `0x1611D0` | 443 | UnwindData |  |
| 325 | `CoRegisterClassObject` | `0x1613A0` | 797 | UnwindData |  |
| 583 | `WdtpInterfacePointer_UserMarshal` | `0x165A80` | 257 | UnwindData |  |
| 584 | `WdtpInterfacePointer_UserMarshal64` | `0x165B90` | 257 | UnwindData |  |
| 91 | `CLIPFORMAT_UserMarshal` | `0x165CA0` | 359 | UnwindData |  |
| 94 | `CLIPFORMAT_UserMarshal64` | `0x165E10` | 388 | UnwindData |  |
| 391 | `HBITMAP_UserMarshal` | `0x165FA0` | 340 | UnwindData |  |
| 392 | `HBITMAP_UserMarshal64` | `0x166100` | 385 | UnwindData |  |
| 415 | `HGLOBAL_UserMarshal` | `0x166290` | 275 | UnwindData |  |
| 416 | `HGLOBAL_UserMarshal64` | `0x1663B0` | 276 | UnwindData |  |
| 202 | *Ordinal Only* | `0x166560` | 554 | UnwindData |  |
| 222 | *Ordinal Only* | `0x166790` | 615 | UnwindData |  |
| 456 | `HSTRING_UserMarshal64` | `0x166B60` | 271 | UnwindData |  |
| 103 | *Ordinal Only* | `0x177A30` | 116 | UnwindData |  |
| 608 | `WindowsTrimStringStart` | `0x179130` | 221 | UnwindData |  |
| 209 | *Ordinal Only* | `0x1794C0` | 442 | UnwindData |  |
| 121 | *Ordinal Only* | `0x17A830` | 269 | UnwindData |  |
| 573 | `RoUnregisterForApartmentShutdown` | `0x17A9C0` | 4,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `RoFailFastWithErrorContext` | `0x17BA60` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `HDC_UserFree` | `0x17BDD0` | 27,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `HRGN_UserFree` | `0x17BDD0` | 27,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `InternalAppInvokeExceptionFilter` | `0x182A10` | 27 | UnwindData |  |
| 473 | `InternalCAggIdSetHandler` | `0x182A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `InternalCCFreeUnused` | `0x182A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `InternalCMLSendReceive` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `InternalCanMakeOutCall` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `InternalCompleteObjRef` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `InternalFillLocalOXIDInfo` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `InternalGetWindowPropInterface` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `InternalMarshalObjRef` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `InternalRegisterWindowPropInterface` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `InternalReleaseMarshalObjRef` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `InternalStubInvoke` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `InternalUnmarshalObjRef` | `0x182A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `InternalCStdIdentityGetInternalUnk` | `0x182A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `InternalCStdIdentityUpdateFlags` | `0x182A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `InternalCallAsProxyExceptionFilter` | `0x182AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `InternalServerExceptionFilter` | `0x182AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `InternalCallFrameExceptionFilter` | `0x182AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `InternalCallerIsAppContainer` | `0x182AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `InternalCoStdMarshalObject` | `0x182AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `InternalDoATClassCreate` | `0x182AF0` | 107 | UnwindData |  |
| 502 | `InternalIrotEnumRunning2` | `0x182B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `InternalOle1ClassFromCLSID2` | `0x182B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `InternalSTAInvoke` | `0x182BA0` | 37,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | *Ordinal Only* | `0x18BF60` | 84 | UnwindData |  |
| 171 | *Ordinal Only* | `0x18BFC0` | 71 | UnwindData |  |
| 135 | *Ordinal Only* | `0x18C280` | 182 | UnwindData |  |
| 134 | *Ordinal Only* | `0x18C340` | 250 | UnwindData |  |
| 162 | *Ordinal Only* | `0x18C440` | 174 | UnwindData |  |
| 230 | *Ordinal Only* | `0x18C500` | 93 | UnwindData |  |
| 286 | `CoGetClassVersion` | `0x18C950` | 232 | UnwindData |  |
| 70 | *Ordinal Only* | `0x18CAD0` | 146 | UnwindData |  |
| 310 | `CoInitializeWOW` | `0x18CB70` | 159 | UnwindData |  |
| 71 | *Ordinal Only* | `0x18CC20` | 282 | UnwindData |  |
| 329 | `CoRegisterMallocSpy` | `0x18D400` | 328 | UnwindData |  |
| 344 | `CoRevokeMallocSpy` | `0x18D550` | 150 | UnwindData |  |
| 226 | *Ordinal Only* | `0x18D5F0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `EnableHookObject` | `0x18DC10` | 76 | UnwindData |  |
| 379 | `GetHookInterface` | `0x18DC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `HkOleRegisterObject` | `0x18DC90` | 34 | UnwindData |  |
| 356 | `CoTreatAsClass` | `0x18E090` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | *Ordinal Only* | `0x18F7D0` | 8,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `UpdateProcessTracing` | `0x191AD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `CoRegisterConsoleHandles` | `0x191BF0` | 241 | UnwindData |  |
| 332 | `CoRegisterRacActivationToken` | `0x191CF0` | 63 | UnwindData |  |
| 341 | `CoRevokeConsoleHandles` | `0x191D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `CoRevokeRacActivationToken` | `0x191D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `UpdateDCOMSettings` | `0x191D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x191D90` | 13,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | *Ordinal Only* | `0x1950D0` | 272 | UnwindData |  |
| 175 | *Ordinal Only* | `0x1951F0` | 272 | UnwindData |  |
| 149 | *Ordinal Only* | `0x195310` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | *Ordinal Only* | `0x195340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x195360` | 366 | UnwindData |  |
| 174 | *Ordinal Only* | `0x1954E0` | 353 | UnwindData |  |
| 346 | `CoSetCancelObject` | `0x196F00` | 142 | UnwindData |  |
| 228 | *Ordinal Only* | `0x196FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | *Ordinal Only* | `0x196FB0` | 27 | UnwindData |  |
| 152 | *Ordinal Only* | `0x196FE0` | 4,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `CoQueryAuthenticationServices` | `0x1981E0` | 553 | UnwindData |  |
| 136 | *Ordinal Only* | `0x198460` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `CoCreateObjectInContext` | `0x198FA0` | 276 | UnwindData |  |
| 267 | `CoDeactivateObject` | `0x199200` | 194 | UnwindData |  |
| 268 | `CoDecodeProxy` | `0x1992D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `CoGetActivationState` | `0x199300` | 47 | UnwindData |  |
| 304 | `CoGetSystemSecurityPermissions` | `0x199340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `CoInvalidateRemoteMachineBindings` | `0x199370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `CoReactivateObject` | `0x199390` | 176 | UnwindData |  |
| 338 | `CoRetireServer` | `0x199450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | *Ordinal Only* | `0x199470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | *Ordinal Only* | `0x199490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | *Ordinal Only* | `0x1994B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | *Ordinal Only* | `0x1994D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `CoSetOutgoingCallState` | `0x1994F0` | 202 | UnwindData |  |
| 125 | *Ordinal Only* | `0x1995C0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | *Ordinal Only* | `0x199790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | *Ordinal Only* | `0x1997B0` | 341 | UnwindData |  |
| 163 | *Ordinal Only* | `0x199C00` | 63 | UnwindData |  |
| 278 | `CoGetApartmentID` | `0x19B060` | 96 | UnwindData |  |
| 138 | *Ordinal Only* | `0x19BC60` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | *Ordinal Only* | `0x19C4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | *Ordinal Only* | `0x19C4C0` | 4,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | *Ordinal Only* | `0x19D610` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | *Ordinal Only* | `0x19D640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `InternalCMLSendReceive2` | `0x19D660` | 224 | UnwindData |  |
| 487 | `InternalCanMakeOutCall2` | `0x19D750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `InternalOleModalLoopBlockFn` | `0x19D770` | 59 | UnwindData |  |
| 526 | `InternalSetAptCallCtrlOnTlsIfRequired` | `0x19D7C0` | 97 | UnwindData |  |
| 318 | `CoPopServiceDomain` | `0x19D8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `CoPushServiceDomain` | `0x19D8C0` | 90 | UnwindData |  |
| 92 | *Ordinal Only* | `0x19E760` | 6,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | *Ordinal Only* | `0x19FFF0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0x1A09C0` | 123 | UnwindData |  |
| 129 | *Ordinal Only* | `0x1A3150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | *Ordinal Only* | `0x1A3170` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | *Ordinal Only* | `0x1A3A60` | 1,213 | UnwindData |  |
| 161 | *Ordinal Only* | `0x1A40A0` | 38 | UnwindData |  |
| 369 | `DllDebugObjectRPCHook` | `0x1A4E20` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `InternalCreateCAggId` | `0x1A5000` | 123 | UnwindData |  |
| 495 | `InternalCreateIdentityHandler` | `0x1A5760` | 75 | UnwindData |  |
| 361 | `CoVrfCheckThreadState` | `0x1BA420` | 1,522 | UnwindData |  |
| 362 | `CoVrfGetThreadState` | `0x1BAA20` | 256 | UnwindData |  |
| 363 | `CoVrfReleaseThreadState` | `0x1BAB30` | 22 | UnwindData |  |
| 145 | *Ordinal Only* | `0x1BB260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | *Ordinal Only* | `0x1BB280` | 23,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `CoAddComDependencyOnPackage` | `0x1C0FD0` | 262 | UnwindData |  |
| 263 | `CoCreateInstanceExFromPackage` | `0x1C10E0` | 161 | UnwindData |  |
| 265 | `CoCreateInstanceFromPackage` | `0x1C1190` | 245 | UnwindData |  |
| 285 | `CoGetClassObjectFromPackage` | `0x1C1290` | 615 | UnwindData |  |
| 227 | *Ordinal Only* | `0x1C1500` | 1,770 | UnwindData |  |
| 292 | `CoGetInstanceFromFile` | `0x1C1BF0` | 425 | UnwindData |  |
| 293 | `CoGetInstanceFromIStorage` | `0x1C1DA0` | 414 | UnwindData |  |
| 225 | *Ordinal Only* | `0x1C7720` | 15,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `InternalCCGetClassInformationForDde` | `0x1CB510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `InternalCCGetClassInformationFromKey` | `0x1CB530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `InternalCCSetDdeServerWindow` | `0x1CB550` | 116 | UnwindData |  |
| 581 | `WdtpInterfacePointer_UserFree` | `0x1CC9C0` | 27 | UnwindData |  |
| 582 | `WdtpInterfacePointer_UserFree64` | `0x1CC9F0` | 2,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | *Ordinal Only* | `0x1CD4D0` | 85 | UnwindData |  |
| 208 | *Ordinal Only* | `0x1CD4D0` | 85 | UnwindData |  |
| 186 | *Ordinal Only* | `0x1CD530` | 243 | UnwindData |  |
| 206 | *Ordinal Only* | `0x1CD630` | 295 | UnwindData |  |
| 185 | *Ordinal Only* | `0x1CD760` | 223 | UnwindData |  |
| 205 | *Ordinal Only* | `0x1CD850` | 268 | UnwindData |  |
| 187 | *Ordinal Only* | `0x1CD970` | 121 | UnwindData |  |
| 207 | *Ordinal Only* | `0x1CD9F0` | 121 | UnwindData |  |
| 192 | *Ordinal Only* | `0x1CDA70` | 164 | UnwindData |  |
| 212 | *Ordinal Only* | `0x1CDA70` | 164 | UnwindData |  |
| 190 | *Ordinal Only* | `0x1CDB20` | 375 | UnwindData |  |
| 210 | *Ordinal Only* | `0x1CDCA0` | 507 | UnwindData |  |
| 189 | *Ordinal Only* | `0x1CDEB0` | 393 | UnwindData |  |
| 191 | *Ordinal Only* | `0x1CE040` | 121 | UnwindData |  |
| 211 | *Ordinal Only* | `0x1CE0C0` | 121 | UnwindData |  |
| 196 | *Ordinal Only* | `0x1CE140` | 85 | UnwindData |  |
| 216 | *Ordinal Only* | `0x1CE140` | 85 | UnwindData |  |
| 194 | *Ordinal Only* | `0x1CE1A0` | 243 | UnwindData |  |
| 214 | *Ordinal Only* | `0x1CE2A0` | 295 | UnwindData |  |
| 193 | *Ordinal Only* | `0x1CE3D0` | 223 | UnwindData |  |
| 213 | *Ordinal Only* | `0x1CE4C0` | 268 | UnwindData |  |
| 195 | *Ordinal Only* | `0x1CE5E0` | 339 | UnwindData |  |
| 215 | *Ordinal Only* | `0x1CE740` | 477 | UnwindData |  |
| 413 | `HGLOBAL_UserFree` | `0x1CE960` | 85 | UnwindData |  |
| 414 | `HGLOBAL_UserFree64` | `0x1CE960` | 85 | UnwindData |  |
| 419 | `HGLOBAL_UserUnmarshal` | `0x1CE9C0` | 129 | UnwindData |  |
| 420 | `HGLOBAL_UserUnmarshal64` | `0x1CEA50` | 129 | UnwindData |  |
| 445 | `HPALETTE_UserFree` | `0x1CEF70` | 85 | UnwindData |  |
| 446 | `HPALETTE_UserFree64` | `0x1CEF70` | 85 | UnwindData |  |
| 447 | `HPALETTE_UserMarshal` | `0x1CEFD0` | 269 | UnwindData |  |
| 448 | `HPALETTE_UserMarshal64` | `0x1CF0F0` | 323 | UnwindData |  |
| 449 | `HPALETTE_UserSize` | `0x1CF240` | 237 | UnwindData |  |
| 450 | `HPALETTE_UserSize64` | `0x1CF340` | 232 | UnwindData |  |
| 451 | `HPALETTE_UserUnmarshal` | `0x1CF430` | 121 | UnwindData |  |
| 452 | `HPALETTE_UserUnmarshal64` | `0x1CF4B0` | 121 | UnwindData |  |
| 200 | *Ordinal Only* | `0x1CF5E0` | 84 | UnwindData |  |
| 220 | *Ordinal Only* | `0x1CF5E0` | 84 | UnwindData |  |
| 198 | *Ordinal Only* | `0x1CF640` | 232 | UnwindData |  |
| 218 | *Ordinal Only* | `0x1CF730` | 235 | UnwindData |  |
| 197 | *Ordinal Only* | `0x1CF830` | 270 | UnwindData |  |
| 217 | *Ordinal Only* | `0x1CF950` | 288 | UnwindData |  |
| 199 | *Ordinal Only* | `0x1CFA80` | 765 | UnwindData |  |
| 219 | *Ordinal Only* | `0x1CFD90` | 789 | UnwindData |  |
| 298 | `CoGetModuleType` | `0x1D15A0` | 219 | UnwindData |  |
| 229 | *Ordinal Only* | `0x1DCFE0` | 108,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | *Ordinal Only* | `0x1F7860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | *Ordinal Only* | `0x1F7880` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `WindowsInspectString` | `0x1F7AA0` | 94 | UnwindData |  |
| 599 | `WindowsInspectString2` | `0x1F7B10` | 77 | UnwindData |  |
| 83 | `RoFailFastWithErrorContextInternal` | `0x1F8160` | 373 | UnwindData |  |
| 556 | `RoInspectCapturedStackBackTrace` | `0x1F8370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `RoInspectThreadErrorInfo` | `0x1F8380` | 159 | UnwindData |  |
| 564 | `RoReportCapabilityCheckFailure` | `0x1F8430` | 51 | UnwindData |  |
| 566 | `RoReportUnhandledError` | `0x1F8470` | 42 | UnwindData |  |
| 567 | `RoResolveRestrictedErrorInfoReference` | `0x1F94E0` | 183 | UnwindData |  |
| 546 | `RoFreeParameterizedTypeExtra` | `0x1FA570` | 38 | UnwindData |  |
| 116 | `CStdAsyncStubBuffer2_Connect` | `0x1FA780` | 61 | UnwindData |  |
| 118 | `CStdAsyncStubBuffer2_Release` | `0x1FA7D0` | 107 | UnwindData |  |
| 131 | `CStdAsyncStubBuffer_Connect` | `0x1FA850` | 69 | UnwindData |  |
| 144 | `CStdAsyncStubBuffer_Invoke` | `0x1FA8A0` | 296 | UnwindData |  |
| 236 | `CStdStubBuffer2_CountRefs` | `0x1FAAB0` | 47 | UnwindData |  |
| 241 | `CStdStubBuffer_CountRefs` | `0x1FAB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `CStdStubBuffer_IsIIDSupported` | `0x1FABB0` | 73 | UnwindData |  |
| 536 | `NdrOleInitializeExtension` | `0x1FB400` | 74 | UnwindData |  |
| 81 | *Ordinal Only* | `0x200930` | 60 | UnwindData |  |
| 170 | *Ordinal Only* | `0x200980` | 236 | UnwindData |  |
| 80 | *Ordinal Only* | `0x200A80` | 64 | UnwindData |  |
| 169 | *Ordinal Only* | `0x200AD0` | 307 | UnwindData |  |
| 79 | *Ordinal Only* | `0x20F6B0` | 433 | UnwindData |  |
| 32 | `NdrProxyForwardingFunction3` | `0x222520` | 71 | UnwindData |  |
| 33 | `NdrProxyForwardingFunction4` | `0x222570` | 71 | UnwindData |  |
| 34 | `NdrProxyForwardingFunction5` | `0x2225C0` | 71 | UnwindData |  |
| 35 | `NdrProxyForwardingFunction6` | `0x222610` | 71 | UnwindData |  |
| 36 | `NdrProxyForwardingFunction7` | `0x222660` | 71 | UnwindData |  |
| 37 | `NdrProxyForwardingFunction8` | `0x2226B0` | 71 | UnwindData |  |
| 38 | `NdrProxyForwardingFunction9` | `0x222700` | 71 | UnwindData |  |
| 39 | `NdrProxyForwardingFunction10` | `0x222750` | 71 | UnwindData |  |
| 40 | `NdrProxyForwardingFunction11` | `0x2227A0` | 71 | UnwindData |  |
| 41 | `NdrProxyForwardingFunction12` | `0x2227F0` | 71 | UnwindData |  |
| 42 | `NdrProxyForwardingFunction13` | `0x222840` | 71 | UnwindData |  |
| 43 | `NdrProxyForwardingFunction14` | `0x222890` | 71 | UnwindData |  |
| 44 | `NdrProxyForwardingFunction15` | `0x2228E0` | 71 | UnwindData |  |
| 45 | `NdrProxyForwardingFunction16` | `0x222930` | 74 | UnwindData |  |
| 46 | `NdrProxyForwardingFunction17` | `0x222980` | 74 | UnwindData |  |
| 47 | `NdrProxyForwardingFunction18` | `0x2229D0` | 74 | UnwindData |  |
| 48 | `NdrProxyForwardingFunction19` | `0x222A20` | 74 | UnwindData |  |
| 49 | `NdrProxyForwardingFunction20` | `0x222A70` | 74 | UnwindData |  |
| 50 | `NdrProxyForwardingFunction21` | `0x222AC0` | 74 | UnwindData |  |
| 51 | `NdrProxyForwardingFunction22` | `0x222B10` | 74 | UnwindData |  |
| 52 | `NdrProxyForwardingFunction23` | `0x222B60` | 74 | UnwindData |  |
| 53 | `NdrProxyForwardingFunction24` | `0x222BB0` | 74 | UnwindData |  |
| 54 | `NdrProxyForwardingFunction25` | `0x222C00` | 74 | UnwindData |  |
| 55 | `NdrProxyForwardingFunction26` | `0x222C50` | 74 | UnwindData |  |
| 56 | `NdrProxyForwardingFunction27` | `0x222CA0` | 74 | UnwindData |  |
| 57 | `NdrProxyForwardingFunction28` | `0x222CF0` | 74 | UnwindData |  |
| 58 | `NdrProxyForwardingFunction29` | `0x222D40` | 74 | UnwindData |  |
| 59 | `NdrProxyForwardingFunction30` | `0x222D90` | 74 | UnwindData |  |
| 60 | `NdrProxyForwardingFunction31` | `0x222DE0` | 74 | UnwindData |  |
| 61 | `NdrProxyForwardingFunction32` | `0x222E30` | 74 | UnwindData |  |
| 2 | `ObjectStublessClient3` | `0x24A440` | 10 | UnwindData |  |
| 3 | `ObjectStublessClient4` | `0x24A450` | 10 | UnwindData |  |
| 4 | `ObjectStublessClient5` | `0x24A460` | 10 | UnwindData |  |
| 5 | `ObjectStublessClient6` | `0x24A470` | 10 | UnwindData |  |
| 6 | `ObjectStublessClient7` | `0x24A480` | 10 | UnwindData |  |
| 7 | `ObjectStublessClient8` | `0x24A490` | 10 | UnwindData |  |
| 8 | `ObjectStublessClient9` | `0x24A4A0` | 10 | UnwindData |  |
| 9 | `ObjectStublessClient10` | `0x24A4B0` | 10 | UnwindData |  |
| 10 | `ObjectStublessClient11` | `0x24A4C0` | 10 | UnwindData |  |
| 11 | `ObjectStublessClient12` | `0x24A4D0` | 10 | UnwindData |  |
| 12 | `ObjectStublessClient13` | `0x24A4E0` | 10 | UnwindData |  |
| 13 | `ObjectStublessClient14` | `0x24A4F0` | 10 | UnwindData |  |
| 14 | `ObjectStublessClient15` | `0x24A500` | 10 | UnwindData |  |
| 15 | `ObjectStublessClient16` | `0x24A510` | 10 | UnwindData |  |
| 16 | `ObjectStublessClient17` | `0x24A520` | 10 | UnwindData |  |
| 17 | `ObjectStublessClient18` | `0x24A530` | 10 | UnwindData |  |
| 18 | `ObjectStublessClient19` | `0x24A540` | 10 | UnwindData |  |
| 19 | `ObjectStublessClient20` | `0x24A550` | 10 | UnwindData |  |
| 20 | `ObjectStublessClient21` | `0x24A560` | 10 | UnwindData |  |
| 21 | `ObjectStublessClient22` | `0x24A570` | 10 | UnwindData |  |
| 22 | `ObjectStublessClient23` | `0x24A580` | 10 | UnwindData |  |
| 23 | `ObjectStublessClient24` | `0x24A590` | 10 | UnwindData |  |
| 24 | `ObjectStublessClient25` | `0x24A5A0` | 10 | UnwindData |  |
| 25 | `ObjectStublessClient26` | `0x24A5B0` | 10 | UnwindData |  |
| 26 | `ObjectStublessClient27` | `0x24A5C0` | 10 | UnwindData |  |
| 27 | `ObjectStublessClient28` | `0x24A5D0` | 10 | UnwindData |  |
| 28 | `ObjectStublessClient29` | `0x24A5E0` | 10 | UnwindData |  |
| 29 | `ObjectStublessClient30` | `0x24A5F0` | 10 | UnwindData |  |
| 30 | `ObjectStublessClient31` | `0x24A600` | 10 | UnwindData |  |
| 31 | `ObjectStublessClient32` | `0x24A610` | 10 | UnwindData |  |
| 183 | *Ordinal Only* | `0x2DA018` | 0 | Indeterminate |  |
