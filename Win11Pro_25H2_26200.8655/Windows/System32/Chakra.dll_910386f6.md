# Binary Specification: Chakra.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Chakra.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `910386f6e256a9bab1325adcdfcf885bb52fd7f75140d7b4dc9c799d890a8dd8`
* **Total Exported Functions:** 160

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 418 | `MemProtectHeapRootAlloc` | `0x2C150` | 322 | UnwindData |  |
| 420 | `MemProtectHeapRootRealloc` | `0x2C730` | 1,061 | UnwindData |  |
| 424 | `MemProtectHeapUnrootAndZero` | `0x24DBC0` | 943 | UnwindData |  |
| 555 | `JsVarAddRef` | `0x2B14C0` | 416 | UnwindData |  |
| 474 | `JsDisposeRuntime` | `0x2BB0C0` | 34 | UnwindData |  |
| 466 | `JsCreateThreadService` | `0x2C37B0` | 125 | UnwindData |  |
| 537 | `JsSetCurrentContext` | `0x2C45C0` | 55 | UnwindData |  |
| 409 | `MemProtectHeapCreate` | `0x2C7130` | 101 | UnwindData |  |
| 415 | `MemProtectHeapProtectCurrentThread` | `0x2C8480` | 55 | UnwindData |  |
| 556 | `JsVarRelease` | `0x2CD850` | 427 | UnwindData |  |
| 450 | `JsConvertValueToString` | `0x2D4E00` | 154 | UnwindData |  |
| 500 | `JsGetPrototype` | `0x2D5150` | 67 | UnwindData |  |
| 532 | `JsRunScript` | `0x2D56B0` | 465 | UnwindData |  |
| 552 | `JsStrictEquals` | `0x2D5DD0` | 83 | UnwindData |  |
| 496 | `JsGetPropertyIdFromName` | `0x2D63F0` | 92 | UnwindData |  |
| 495 | `JsGetProperty` | `0x2D6530` | 83 | UnwindData |  |
| 544 | `JsSetProperty` | `0x2D66B0` | 95 | UnwindData |  |
| 444 | `JsCallFunction` | `0x2D6720` | 109 | UnwindData |  |
| 529 | `JsPointerToString` | `0x2D68B0` | 83 | UnwindData |  |
| 442 | `JsBoolToBoolean` | `0x2D6B00` | 67 | UnwindData |  |
| 542 | `JsSetObjectBeforeCollectCallback` | `0x308AD0` | 202 | UnwindData |  |
| 441 | `JsAddRef` | `0x308C30` | 215 | UnwindData |  |
| 531 | `JsRelease` | `0x308D80` | 219 | UnwindData |  |
| 557 | `JsVarToExtension` | `0x30CF30` | 117 | UnwindData |  |
| 435 | `RecyclerNativeHeapRootAddRef` | `0x310200` | 84 | UnwindData |  |
| 436 | `RecyclerNativeHeapRootRelease` | `0x310260` | 62 | UnwindData |  |
| 432 | `RecyclerNativeHeapGetRealAddressFromInterior` | `0x310980` | 118 | UnwindData |  |
| 510 | `JsGetValueType` | `0x31A930` | 42,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `JsStringToPointer` | `0x324EB0` | 123 | UnwindData |  |
| 539 | `JsSetExternalData` | `0x3325B0` | 68 | UnwindData |  |
| 486 | `JsGetExternalData` | `0x332600` | 84 | UnwindData |  |
| 417 | `MemProtectHeapReportHeapSize` | `0x33AE00` | 179 | UnwindData |  |
| 523 | `JsNumberToInt` | `0x34CE40` | 114 | UnwindData |  |
| 428 | `RecyclerNativeHeapAllocTraced` | `0x35A470` | 24 | UnwindData |  |
| 429 | `RecyclerNativeHeapAllocTracedFinalized` | `0x35EB10` | 24 | UnwindData |  |
| 414 | `MemProtectHeapNotifyCurrentThreadDetach` | `0x372C40` | 89 | UnwindData |  |
| 483 | `JsGetCurrentContext` | `0x378A00` | 29,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `JsQueueBackgroundParse` | `0x37FD50` | 94 | UnwindData |  |
| 437 | `DllCanUnloadNow` | `0x3853E0` | 212 | UnwindData |  |
| 438 | `DllGetClassObject` | `0x387D70` | 288 | UnwindData |  |
| 443 | `JsBooleanToBool` | `0x38E100` | 85 | UnwindData |  |
| 511 | `JsHasException` | `0x3978B0` | 4,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `JsGetPropertyNameFromId` | `0x398C00` | 46 | UnwindData |  |
| 459 | `JsCreateNamedFunction` | `0x3A1B20` | 39 | UnwindData |  |
| 473 | `JsDisableRuntimeExecution` | `0x3A2830` | 19,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `JsCreateFunction` | `0x3A74C0` | 36 | UnwindData |  |
| 457 | `JsCreateExternalObject` | `0x3A9820` | 31 | UnwindData |  |
| 545 | `JsSetPrototype` | `0x3A9F30` | 67 | UnwindData |  |
| 475 | `JsDoubleToNumber` | `0x3B9250` | 87 | UnwindData |  |
| 538 | `JsSetException` | `0x3CAE00` | 55 | UnwindData |  |
| 488 | `JsGetGlobalObject` | `0x3CB230` | 34 | UnwindData |  |
| 515 | `JsHasProperty` | `0x3D11B0` | 234 | UnwindData |  |
| 451 | `JsCreateArray` | `0x3D6BB0` | 67 | UnwindData |  |
| 402 | `CreateChakraEngine` | `0x3F2360` | 312 | UnwindData |  |
| 404 | `JsDiscardBackgroundParse` | `0x3F4DB0` | 74 | UnwindData |  |
| 558 | `JsVarToScriptDirect` | `0x3F7450` | 129 | UnwindData |  |
| 403 | `DumpDiagInfo` | `0x3F7610` | 32 | UnwindData |  |
| 439 | `DllRegisterServer` | `0x3F7640` | 177 | UnwindData |  |
| 440 | `DllUnregisterServer` | `0x3F7700` | 175 | UnwindData |  |
| 445 | `JsCollectGarbage` | `0x4425E0` | 41 | UnwindData |  |
| 446 | `JsConstructObject` | `0x442610` | 96 | UnwindData |  |
| 447 | `JsConvertValueToBoolean` | `0x442680` | 67 | UnwindData |  |
| 448 | `JsConvertValueToNumber` | `0x4426D0` | 67 | UnwindData |  |
| 449 | `JsConvertValueToObject` | `0x442720` | 67 | UnwindData |  |
| 452 | `JsCreateArrayBuffer` | `0x442770` | 67 | UnwindData |  |
| 453 | `JsCreateContext` | `0x4427C0` | 67 | UnwindData |  |
| 454 | `JsCreateDataView` | `0x442810` | 94 | UnwindData |  |
| 455 | `JsCreateError` | `0x442880` | 67 | UnwindData |  |
| 456 | `JsCreateExternalArrayBuffer` | `0x4428D0` | 102 | UnwindData |  |
| 460 | `JsCreateObject` | `0x442940` | 55 | UnwindData |  |
| 461 | `JsCreateRangeError` | `0x442980` | 67 | UnwindData |  |
| 462 | `JsCreateReferenceError` | `0x4429D0` | 67 | UnwindData |  |
| 463 | `JsCreateRuntime` | `0x442A20` | 100 | UnwindData |  |
| 464 | `JsCreateSymbol` | `0x442A90` | 67 | UnwindData |  |
| 465 | `JsCreateSyntaxError` | `0x442AE0` | 67 | UnwindData |  |
| 467 | `JsCreateTypeError` | `0x442B30` | 67 | UnwindData |  |
| 468 | `JsCreateTypedArray` | `0x442B80` | 102 | UnwindData |  |
| 469 | `JsCreateURIError` | `0x442BF0` | 67 | UnwindData |  |
| 470 | `JsDefineProperty` | `0x442C40` | 95 | UnwindData |  |
| 471 | `JsDeleteIndexedProperty` | `0x442CB0` | 67 | UnwindData |  |
| 472 | `JsDeleteProperty` | `0x442D00` | 95 | UnwindData |  |
| 476 | `JsEnableRuntimeExecution` | `0x442D70` | 34 | UnwindData |  |
| 478 | `JsEquals` | `0x442DA0` | 83 | UnwindData |  |
| 479 | `JsGetAndClearException` | `0x442E00` | 271 | UnwindData |  |
| 480 | `JsGetArrayBufferStorage` | `0x442F20` | 133 | UnwindData |  |
| 481 | `JsGetContextData` | `0x442FB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `JsGetContextOfObject` | `0x442FF0` | 114 | UnwindData |  |
| 484 | `JsGetDataViewStorage` | `0x443070` | 137 | UnwindData |  |
| 485 | `JsGetExtensionAllowed` | `0x443100` | 67 | UnwindData |  |
| 487 | `JsGetFalseValue` | `0x443150` | 34 | UnwindData |  |
| 489 | `JsGetIndexedPropertiesExternalData` | `0x443180` | 649 | UnwindData |  |
| 490 | `JsGetIndexedProperty` | `0x443410` | 83 | UnwindData |  |
| 491 | `JsGetNullValue` | `0x443470` | 34 | UnwindData |  |
| 492 | `JsGetOwnPropertyDescriptor` | `0x4434A0` | 83 | UnwindData |  |
| 493 | `JsGetOwnPropertyNames` | `0x443500` | 67 | UnwindData |  |
| 494 | `JsGetOwnPropertySymbols` | `0x443550` | 67 | UnwindData |  |
| 497 | `JsGetPropertyIdFromSymbol` | `0x4435A0` | 67 | UnwindData |  |
| 498 | `JsGetPropertyIdType` | `0x4435F0` | 46 | UnwindData |  |
| 501 | `JsGetRuntime` | `0x443630` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `JsGetRuntimeMemoryLimit` | `0x443680` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `JsGetRuntimeMemoryUsage` | `0x4436D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `JsGetStringLength` | `0x443720` | 81 | UnwindData |  |
| 505 | `JsGetSymbolFromPropertyId` | `0x443780` | 67 | UnwindData |  |
| 506 | `JsGetTrueValue` | `0x4437D0` | 34 | UnwindData |  |
| 507 | `JsGetTypedArrayInfo` | `0x443800` | 157 | UnwindData |  |
| 508 | `JsGetTypedArrayStorage` | `0x4438B0` | 272 | UnwindData |  |
| 509 | `JsGetUndefinedValue` | `0x4439D0` | 34 | UnwindData |  |
| 512 | `JsHasExternalData` | `0x443A00` | 63 | UnwindData |  |
| 513 | `JsHasIndexedPropertiesExternalData` | `0x443A50` | 130 | UnwindData |  |
| 514 | `JsHasIndexedProperty` | `0x443AE0` | 83 | UnwindData |  |
| 516 | `JsIdle` | `0x443B40` | 50 | UnwindData |  |
| 518 | `JsInstanceOf` | `0x443B80` | 83 | UnwindData |  |
| 519 | `JsIntToNumber` | `0x443BE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `JsIsRuntimeExecutionDisabled` | `0x443C20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `JsNumberToDouble` | `0x443C80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `JsParseScript` | `0x443CF0` | 49 | UnwindData |  |
| 526 | `JsParseScriptWithAttributes` | `0x443D30` | 54 | UnwindData |  |
| 527 | `JsParseSerializedScript` | `0x443D70` | 85 | UnwindData |  |
| 528 | `JsParseSerializedScriptWithCallback` | `0x443DD0` | 74 | UnwindData |  |
| 530 | `JsPreventExtension` | `0x443E20` | 55 | UnwindData |  |
| 533 | `JsRunSerializedScript` | `0x443E60` | 85 | UnwindData |  |
| 534 | `JsRunSerializedScriptWithCallback` | `0x443EC0` | 74 | UnwindData |  |
| 535 | `JsSerializeScript` | `0x443F10` | 67 | UnwindData |  |
| 536 | `JsSetContextData` | `0x443F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `JsSetIndexedPropertiesToExternalData` | `0x443FA0` | 95 | UnwindData |  |
| 541 | `JsSetIndexedProperty` | `0x444010` | 83 | UnwindData |  |
| 543 | `JsSetPromiseContinuationCallback` | `0x444070` | 46 | UnwindData |  |
| 546 | `JsSetRuntimeBeforeCollectCallback` | `0x4440B0` | 58 | UnwindData |  |
| 547 | `JsSetRuntimeMemoryAllocationCallback` | `0x4440F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `JsSetRuntimeMemoryLimit` | `0x444140` | 18,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `JsEnumerateHeap` | `0x448AF0` | 130 | UnwindData |  |
| 517 | `JsInspectableToObject` | `0x448B80` | 46 | UnwindData |  |
| 520 | `JsIsEnumeratingHeap` | `0x448BC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `JsObjectToInspectable` | `0x448C30` | 46 | UnwindData |  |
| 400 | `JsProjectWinRTNamespace` | `0x448C70` | 34 | UnwindData |  |
| 401 | `JsSetProjectionEnqueueCallback` | `0x448CA0` | 46 | UnwindData |  |
| 549 | `JsStartDebugging` | `0x448CE0` | 15 | UnwindData |  |
| 550 | `JsStartProfiling` | `0x448D00` | 58 | UnwindData |  |
| 551 | `JsStopProfiling` | `0x448D40` | 34 | UnwindData |  |
| 554 | `JsValueToVariant` | `0x448D70` | 46 | UnwindData |  |
| 559 | `JsVariantToValue` | `0x448DB0` | 46 | UnwindData |  |
| 407 | `MemProtectHeapAddRootSection` | `0x474AA0` | 159 | UnwindData |  |
| 408 | `MemProtectHeapCollect` | `0x474B50` | 154 | UnwindData |  |
| 410 | `MemProtectHeapDestroy` | `0x474BF0` | 60 | UnwindData |  |
| 411 | `MemProtectHeapDisableCollection` | `0x474C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `MemProtectHeapIsValidObject` | `0x474C60` | 234 | UnwindData |  |
| 413 | `MemProtectHeapMemSize` | `0x474D50` | 229 | UnwindData |  |
| 416 | `MemProtectHeapRemoveRootSection` | `0x474E40` | 170 | UnwindData |  |
| 419 | `MemProtectHeapRootAllocLeaf` | `0x474EF0` | 184 | UnwindData |  |
| 421 | `MemProtectHeapRootReallocLeaf` | `0x474FB0` | 181 | UnwindData |  |
| 422 | `MemProtectHeapSynchronizeWithCollector` | `0x475070` | 75 | UnwindData |  |
| 423 | `MemProtectHeapUnprotectCurrentThread` | `0x4750D0` | 40 | UnwindData |  |
| 425 | `RecyclerNativeHeapAddExternalMemoryUsage` | `0x475260` | 24 | UnwindData |  |
| 426 | `RecyclerNativeHeapAllocLeaf` | `0x475280` | 24 | UnwindData |  |
| 427 | `RecyclerNativeHeapAllocLeafFinalized` | `0x4752A0` | 24 | UnwindData |  |
| 430 | `RecyclerNativeHeapCollectGarbageInThread` | `0x4752C0` | 36 | UnwindData |  |
| 431 | `RecyclerNativeHeapCreateWeakReference` | `0x4752F0` | 88 | UnwindData |  |
| 433 | `RecyclerNativeHeapGetStrongReference` | `0x475350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `RecyclerNativeHeapHasWeakReferenceCleanupOccurred` | `0x475370` | 932,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `JsInitializeJITServer` | `0x558D90` | 260 | UnwindData |  |
