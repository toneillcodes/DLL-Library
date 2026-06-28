# Binary Specification: Chakra.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Chakra.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ad400f10d384c9879e3aee6c130193028766fa4caf5d77de33d42da83b419ce8`
* **Total Exported Functions:** 160

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 418 | `MemProtectHeapRootAlloc` | `0x5E860` | 322 | UnwindData |  |
| 420 | `MemProtectHeapRootRealloc` | `0x5EE40` | 1,061 | UnwindData |  |
| 417 | `MemProtectHeapReportHeapSize` | `0x60140` | 179 | UnwindData |  |
| 424 | `MemProtectHeapUnrootAndZero` | `0x602C0` | 943 | UnwindData |  |
| 555 | `JsVarAddRef` | `0xC30F0` | 416 | UnwindData |  |
| 542 | `JsSetObjectBeforeCollectCallback` | `0x2ADE20` | 202 | UnwindData |  |
| 466 | `JsCreateThreadService` | `0x2AE670` | 125 | UnwindData |  |
| 537 | `JsSetCurrentContext` | `0x2AF470` | 55 | UnwindData |  |
| 441 | `JsAddRef` | `0x2AF740` | 215 | UnwindData |  |
| 531 | `JsRelease` | `0x2AF890` | 219 | UnwindData |  |
| 409 | `MemProtectHeapCreate` | `0x2B2220` | 101 | UnwindData |  |
| 415 | `MemProtectHeapProtectCurrentThread` | `0x2B3FC0` | 55 | UnwindData |  |
| 556 | `JsVarRelease` | `0x2C1DD0` | 427 | UnwindData |  |
| 450 | `JsConvertValueToString` | `0x2C32C0` | 154 | UnwindData |  |
| 500 | `JsGetPrototype` | `0x2C3610` | 67 | UnwindData |  |
| 532 | `JsRunScript` | `0x2C3B70` | 465 | UnwindData |  |
| 552 | `JsStrictEquals` | `0x2C4290` | 83 | UnwindData |  |
| 496 | `JsGetPropertyIdFromName` | `0x2C48B0` | 92 | UnwindData |  |
| 495 | `JsGetProperty` | `0x2C49F0` | 83 | UnwindData |  |
| 544 | `JsSetProperty` | `0x2C4B70` | 95 | UnwindData |  |
| 444 | `JsCallFunction` | `0x2C4BE0` | 109 | UnwindData |  |
| 529 | `JsPointerToString` | `0x2C4D70` | 83 | UnwindData |  |
| 442 | `JsBoolToBoolean` | `0x2C4FC0` | 67 | UnwindData |  |
| 557 | `JsVarToExtension` | `0x301610` | 117 | UnwindData |  |
| 435 | `RecyclerNativeHeapRootAddRef` | `0x303070` | 84 | UnwindData |  |
| 436 | `RecyclerNativeHeapRootRelease` | `0x3030D0` | 62 | UnwindData |  |
| 432 | `RecyclerNativeHeapGetRealAddressFromInterior` | `0x303920` | 118 | UnwindData |  |
| 510 | `JsGetValueType` | `0x30EA90` | 42,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `JsDisposeRuntime` | `0x318F90` | 34 | UnwindData |  |
| 553 | `JsStringToPointer` | `0x31A040` | 123 | UnwindData |  |
| 539 | `JsSetExternalData` | `0x326C00` | 68 | UnwindData |  |
| 486 | `JsGetExternalData` | `0x326C50` | 84 | UnwindData |  |
| 523 | `JsNumberToInt` | `0x342970` | 114 | UnwindData |  |
| 428 | `RecyclerNativeHeapAllocTraced` | `0x3506E0` | 24 | UnwindData |  |
| 429 | `RecyclerNativeHeapAllocTracedFinalized` | `0x353A40` | 24 | UnwindData |  |
| 414 | `MemProtectHeapNotifyCurrentThreadDetach` | `0x3696F0` | 89 | UnwindData |  |
| 483 | `JsGetCurrentContext` | `0x36F4F0` | 27,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `JsQueueBackgroundParse` | `0x375F60` | 94 | UnwindData |  |
| 437 | `DllCanUnloadNow` | `0x37B6E0` | 212 | UnwindData |  |
| 438 | `DllGetClassObject` | `0x37DD50` | 288 | UnwindData |  |
| 443 | `JsBooleanToBool` | `0x383B50` | 85 | UnwindData |  |
| 511 | `JsHasException` | `0x38CD20` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `JsGetPropertyNameFromId` | `0x38E1D0` | 46 | UnwindData |  |
| 459 | `JsCreateNamedFunction` | `0x397040` | 39 | UnwindData |  |
| 473 | `JsDisableRuntimeExecution` | `0x3984E0` | 17,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `JsCreateFunction` | `0x39CA70` | 36 | UnwindData |  |
| 457 | `JsCreateExternalObject` | `0x39EE50` | 31 | UnwindData |  |
| 545 | `JsSetPrototype` | `0x39F560` | 67 | UnwindData |  |
| 475 | `JsDoubleToNumber` | `0x3AE200` | 87 | UnwindData |  |
| 538 | `JsSetException` | `0x3BFBE0` | 55 | UnwindData |  |
| 488 | `JsGetGlobalObject` | `0x3C0010` | 34 | UnwindData |  |
| 515 | `JsHasProperty` | `0x3C5D10` | 234 | UnwindData |  |
| 451 | `JsCreateArray` | `0x3CB760` | 67 | UnwindData |  |
| 402 | `CreateChakraEngine` | `0x3E7760` | 312 | UnwindData |  |
| 404 | `JsDiscardBackgroundParse` | `0x3EA060` | 74 | UnwindData |  |
| 558 | `JsVarToScriptDirect` | `0x3EC6D0` | 129 | UnwindData |  |
| 403 | `DumpDiagInfo` | `0x3EC890` | 32 | UnwindData |  |
| 439 | `DllRegisterServer` | `0x3EC8C0` | 177 | UnwindData |  |
| 440 | `DllUnregisterServer` | `0x3EC980` | 175 | UnwindData |  |
| 445 | `JsCollectGarbage` | `0x4482C0` | 41 | UnwindData |  |
| 446 | `JsConstructObject` | `0x4482F0` | 96 | UnwindData |  |
| 447 | `JsConvertValueToBoolean` | `0x448360` | 67 | UnwindData |  |
| 448 | `JsConvertValueToNumber` | `0x4483B0` | 67 | UnwindData |  |
| 449 | `JsConvertValueToObject` | `0x448400` | 67 | UnwindData |  |
| 452 | `JsCreateArrayBuffer` | `0x448450` | 67 | UnwindData |  |
| 453 | `JsCreateContext` | `0x4484A0` | 67 | UnwindData |  |
| 454 | `JsCreateDataView` | `0x4484F0` | 94 | UnwindData |  |
| 455 | `JsCreateError` | `0x448560` | 67 | UnwindData |  |
| 456 | `JsCreateExternalArrayBuffer` | `0x4485B0` | 102 | UnwindData |  |
| 460 | `JsCreateObject` | `0x448620` | 55 | UnwindData |  |
| 461 | `JsCreateRangeError` | `0x448660` | 67 | UnwindData |  |
| 462 | `JsCreateReferenceError` | `0x4486B0` | 67 | UnwindData |  |
| 463 | `JsCreateRuntime` | `0x448700` | 100 | UnwindData |  |
| 464 | `JsCreateSymbol` | `0x448770` | 67 | UnwindData |  |
| 465 | `JsCreateSyntaxError` | `0x4487C0` | 67 | UnwindData |  |
| 467 | `JsCreateTypeError` | `0x448810` | 67 | UnwindData |  |
| 468 | `JsCreateTypedArray` | `0x448860` | 102 | UnwindData |  |
| 469 | `JsCreateURIError` | `0x4488D0` | 67 | UnwindData |  |
| 470 | `JsDefineProperty` | `0x448920` | 95 | UnwindData |  |
| 471 | `JsDeleteIndexedProperty` | `0x448990` | 67 | UnwindData |  |
| 472 | `JsDeleteProperty` | `0x4489E0` | 95 | UnwindData |  |
| 476 | `JsEnableRuntimeExecution` | `0x448A50` | 34 | UnwindData |  |
| 478 | `JsEquals` | `0x448A80` | 83 | UnwindData |  |
| 479 | `JsGetAndClearException` | `0x448AE0` | 271 | UnwindData |  |
| 480 | `JsGetArrayBufferStorage` | `0x448C00` | 133 | UnwindData |  |
| 481 | `JsGetContextData` | `0x448C90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `JsGetContextOfObject` | `0x448CD0` | 114 | UnwindData |  |
| 484 | `JsGetDataViewStorage` | `0x448D50` | 137 | UnwindData |  |
| 485 | `JsGetExtensionAllowed` | `0x448DE0` | 67 | UnwindData |  |
| 487 | `JsGetFalseValue` | `0x448E30` | 34 | UnwindData |  |
| 489 | `JsGetIndexedPropertiesExternalData` | `0x448E60` | 649 | UnwindData |  |
| 490 | `JsGetIndexedProperty` | `0x4490F0` | 83 | UnwindData |  |
| 491 | `JsGetNullValue` | `0x449150` | 34 | UnwindData |  |
| 492 | `JsGetOwnPropertyDescriptor` | `0x449180` | 83 | UnwindData |  |
| 493 | `JsGetOwnPropertyNames` | `0x4491E0` | 67 | UnwindData |  |
| 494 | `JsGetOwnPropertySymbols` | `0x449230` | 67 | UnwindData |  |
| 497 | `JsGetPropertyIdFromSymbol` | `0x449280` | 67 | UnwindData |  |
| 498 | `JsGetPropertyIdType` | `0x4492D0` | 46 | UnwindData |  |
| 501 | `JsGetRuntime` | `0x449310` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `JsGetRuntimeMemoryLimit` | `0x449360` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `JsGetRuntimeMemoryUsage` | `0x4493B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `JsGetStringLength` | `0x449400` | 81 | UnwindData |  |
| 505 | `JsGetSymbolFromPropertyId` | `0x449460` | 67 | UnwindData |  |
| 506 | `JsGetTrueValue` | `0x4494B0` | 34 | UnwindData |  |
| 507 | `JsGetTypedArrayInfo` | `0x4494E0` | 157 | UnwindData |  |
| 508 | `JsGetTypedArrayStorage` | `0x449590` | 272 | UnwindData |  |
| 509 | `JsGetUndefinedValue` | `0x4496B0` | 34 | UnwindData |  |
| 512 | `JsHasExternalData` | `0x4496E0` | 63 | UnwindData |  |
| 513 | `JsHasIndexedPropertiesExternalData` | `0x449730` | 130 | UnwindData |  |
| 514 | `JsHasIndexedProperty` | `0x4497C0` | 83 | UnwindData |  |
| 516 | `JsIdle` | `0x449820` | 50 | UnwindData |  |
| 518 | `JsInstanceOf` | `0x449860` | 83 | UnwindData |  |
| 519 | `JsIntToNumber` | `0x4498C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `JsIsRuntimeExecutionDisabled` | `0x449900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `JsNumberToDouble` | `0x449960` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `JsParseScript` | `0x4499D0` | 49 | UnwindData |  |
| 526 | `JsParseScriptWithAttributes` | `0x449A10` | 54 | UnwindData |  |
| 527 | `JsParseSerializedScript` | `0x449A50` | 85 | UnwindData |  |
| 528 | `JsParseSerializedScriptWithCallback` | `0x449AB0` | 74 | UnwindData |  |
| 530 | `JsPreventExtension` | `0x449B00` | 55 | UnwindData |  |
| 533 | `JsRunSerializedScript` | `0x449B40` | 85 | UnwindData |  |
| 534 | `JsRunSerializedScriptWithCallback` | `0x449BA0` | 74 | UnwindData |  |
| 535 | `JsSerializeScript` | `0x449BF0` | 67 | UnwindData |  |
| 536 | `JsSetContextData` | `0x449C40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `JsSetIndexedPropertiesToExternalData` | `0x449C80` | 95 | UnwindData |  |
| 541 | `JsSetIndexedProperty` | `0x449CF0` | 83 | UnwindData |  |
| 543 | `JsSetPromiseContinuationCallback` | `0x449D50` | 46 | UnwindData |  |
| 546 | `JsSetRuntimeBeforeCollectCallback` | `0x449D90` | 58 | UnwindData |  |
| 547 | `JsSetRuntimeMemoryAllocationCallback` | `0x449DD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `JsSetRuntimeMemoryLimit` | `0x449E20` | 29,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `JsEnumerateHeap` | `0x4510B0` | 130 | UnwindData |  |
| 517 | `JsInspectableToObject` | `0x451140` | 57 | UnwindData |  |
| 520 | `JsIsEnumeratingHeap` | `0x451180` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `JsObjectToInspectable` | `0x4511F0` | 57 | UnwindData |  |
| 400 | `JsProjectWinRTNamespace` | `0x451230` | 38 | UnwindData |  |
| 401 | `JsSetProjectionEnqueueCallback` | `0x451260` | 57 | UnwindData |  |
| 549 | `JsStartDebugging` | `0x4512A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `JsStartProfiling` | `0x4512B0` | 74 | UnwindData |  |
| 551 | `JsStopProfiling` | `0x451300` | 37 | UnwindData |  |
| 554 | `JsValueToVariant` | `0x451330` | 57 | UnwindData |  |
| 559 | `JsVariantToValue` | `0x451370` | 57 | UnwindData |  |
| 407 | `MemProtectHeapAddRootSection` | `0x47FE20` | 159 | UnwindData |  |
| 408 | `MemProtectHeapCollect` | `0x47FED0` | 154 | UnwindData |  |
| 410 | `MemProtectHeapDestroy` | `0x47FF70` | 60 | UnwindData |  |
| 411 | `MemProtectHeapDisableCollection` | `0x47FFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `MemProtectHeapIsValidObject` | `0x47FFE0` | 234 | UnwindData |  |
| 413 | `MemProtectHeapMemSize` | `0x4800D0` | 229 | UnwindData |  |
| 416 | `MemProtectHeapRemoveRootSection` | `0x4801C0` | 170 | UnwindData |  |
| 419 | `MemProtectHeapRootAllocLeaf` | `0x480270` | 184 | UnwindData |  |
| 421 | `MemProtectHeapRootReallocLeaf` | `0x480330` | 181 | UnwindData |  |
| 422 | `MemProtectHeapSynchronizeWithCollector` | `0x4803F0` | 75 | UnwindData |  |
| 423 | `MemProtectHeapUnprotectCurrentThread` | `0x480450` | 40 | UnwindData |  |
| 425 | `RecyclerNativeHeapAddExternalMemoryUsage` | `0x4805E0` | 24 | UnwindData |  |
| 426 | `RecyclerNativeHeapAllocLeaf` | `0x480600` | 24 | UnwindData |  |
| 427 | `RecyclerNativeHeapAllocLeafFinalized` | `0x480620` | 24 | UnwindData |  |
| 430 | `RecyclerNativeHeapCollectGarbageInThread` | `0x480640` | 36 | UnwindData |  |
| 431 | `RecyclerNativeHeapCreateWeakReference` | `0x480670` | 88 | UnwindData |  |
| 433 | `RecyclerNativeHeapGetStrongReference` | `0x4806D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `RecyclerNativeHeapHasWeakReferenceCleanupOccurred` | `0x4806F0` | 935,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `JsInitializeJITServer` | `0x564F10` | 260 | UnwindData |  |
