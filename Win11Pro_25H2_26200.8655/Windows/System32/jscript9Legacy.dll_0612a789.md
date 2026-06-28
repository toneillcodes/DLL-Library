# Binary Specification: jscript9Legacy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\jscript9Legacy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0612a789a8be4a925db6d51f3f90d264b9153df7c11f2b5072a8d4297c2313ca`
* **Total Exported Functions:** 97

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3FEA0` | 226 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x3FF90` | 904 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x40480` | 113 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x40500` | 111 | UnwindData |  |
| 5 | `JsAddRef` | `0x5F720` | 46 | UnwindData |  |
| 6 | `JsBoolToBoolean` | `0x5F760` | 46 | UnwindData |  |
| 7 | `JsBooleanToBool` | `0x5F7A0` | 46 | UnwindData |  |
| 8 | `JsCallFunction` | `0x5F7E0` | 71 | UnwindData |  |
| 9 | `JsCollectGarbage` | `0x5F830` | 25 | UnwindData |  |
| 10 | `JsConstructObject` | `0x5F850` | 71 | UnwindData |  |
| 11 | `JsConvertValueToBoolean` | `0x5F8A0` | 46 | UnwindData |  |
| 12 | `JsConvertValueToNumber` | `0x5F8E0` | 46 | UnwindData |  |
| 13 | `JsConvertValueToObject` | `0x5F920` | 46 | UnwindData |  |
| 14 | `JsConvertValueToString` | `0x5F960` | 46 | UnwindData |  |
| 15 | `JsCreateArray` | `0x5F9A0` | 46 | UnwindData |  |
| 16 | `JsCreateContext` | `0x5F9E0` | 58 | UnwindData |  |
| 17 | `JsCreateError` | `0x5FA20` | 46 | UnwindData |  |
| 18 | `JsCreateExternalObject` | `0x5FA60` | 58 | UnwindData |  |
| 19 | `JsCreateExternalType` | `0x5FAA0` | 46 | UnwindData |  |
| 20 | `JsCreateFunction` | `0x5FAE0` | 58 | UnwindData |  |
| 21 | `JsCreateObject` | `0x5FB20` | 25 | UnwindData |  |
| 22 | `JsCreateRangeError` | `0x5FB40` | 46 | UnwindData |  |
| 23 | `JsCreateReferenceError` | `0x5FB80` | 46 | UnwindData |  |
| 24 | `JsCreateRuntime` | `0x5FBC0` | 70 | UnwindData |  |
| 25 | `JsCreateSyntaxError` | `0x5FC10` | 46 | UnwindData |  |
| 26 | `JsCreateTypeError` | `0x5FC50` | 46 | UnwindData |  |
| 27 | `JsCreateTypedExternalObject` | `0x5FC90` | 58 | UnwindData |  |
| 28 | `JsCreateURIError` | `0x5FCD0` | 46 | UnwindData |  |
| 29 | `JsDefineProperty` | `0x5FD10` | 70 | UnwindData |  |
| 30 | `JsDeleteIndexedProperty` | `0x5FD60` | 46 | UnwindData |  |
| 31 | `JsDeleteProperty` | `0x5FDA0` | 70 | UnwindData |  |
| 32 | `JsDisableRuntimeExecution` | `0x5FDF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `JsDisposeRuntime` | `0x5FE50` | 25 | UnwindData |  |
| 34 | `JsDoubleToNumber` | `0x5FE70` | 48 | UnwindData |  |
| 35 | `JsEnableRuntimeExecution` | `0x5FEB0` | 25 | UnwindData |  |
| 36 | `JsEnumerateHeap` | `0x5FED0` | 112 | UnwindData |  |
| 37 | `JsEquals` | `0x5FF50` | 58 | UnwindData |  |
| 38 | `JsGetAndClearException` | `0x5FF90` | 192 | UnwindData |  |
| 39 | `JsGetCurrentContext` | `0x60060` | 57 | UnwindData |  |
| 40 | `JsGetDefaultTypeDescription` | `0x600A0` | 25 | UnwindData |  |
| 41 | `JsGetExtensionAllowed` | `0x600C0` | 46 | UnwindData |  |
| 42 | `JsGetExternalData` | `0x60100` | 46 | UnwindData |  |
| 43 | `JsGetExternalType` | `0x60140` | 46 | UnwindData |  |
| 44 | `JsGetFalseValue` | `0x60180` | 25 | UnwindData |  |
| 45 | `JsGetGlobalObject` | `0x601A0` | 25 | UnwindData |  |
| 46 | `JsGetIndexedProperty` | `0x601C0` | 58 | UnwindData |  |
| 47 | `JsGetNullValue` | `0x60200` | 25 | UnwindData |  |
| 48 | `JsGetOwnPropertyDescriptor` | `0x60220` | 58 | UnwindData |  |
| 49 | `JsGetOwnPropertyNames` | `0x60260` | 46 | UnwindData |  |
| 50 | `JsGetProperty` | `0x602A0` | 58 | UnwindData |  |
| 51 | `JsGetPropertyIdFromName` | `0x602E0` | 46 | UnwindData |  |
| 52 | `JsGetPropertyNameFromId` | `0x60320` | 46 | UnwindData |  |
| 53 | `JsGetPrototype` | `0x60360` | 46 | UnwindData |  |
| 54 | `JsGetRuntime` | `0x603A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `JsGetRuntimeMemoryLimit` | `0x603F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `JsGetRuntimeMemoryUsage` | `0x60430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `JsGetStringLength` | `0x60470` | 46 | UnwindData |  |
| 58 | `JsGetTrueValue` | `0x604B0` | 25 | UnwindData |  |
| 59 | `JsGetUndefinedValue` | `0x604D0` | 25 | UnwindData |  |
| 60 | `JsGetValueType` | `0x604F0` | 46 | UnwindData |  |
| 61 | `JsHasException` | `0x60530` | 165 | UnwindData |  |
| 62 | `JsHasExternalData` | `0x605E0` | 46 | UnwindData |  |
| 63 | `JsHasIndexedProperty` | `0x60620` | 58 | UnwindData |  |
| 64 | `JsHasProperty` | `0x60660` | 58 | UnwindData |  |
| 65 | `JsIdle` | `0x606A0` | 25 | UnwindData |  |
| 66 | `JsIntToNumber` | `0x606C0` | 46 | UnwindData |  |
| 67 | `JsIsEnumeratingHeap` | `0x60700` | 89 | UnwindData |  |
| 68 | `JsIsRuntimeExecutionDisabled` | `0x60760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `JsNumberToDouble` | `0x607A0` | 46 | UnwindData |  |
| 70 | `JsParseScript` | `0x607E0` | 44 | UnwindData |  |
| 71 | `JsParseSerializedScript` | `0x60820` | 48 | UnwindData |  |
| 72 | `JsPointerToString` | `0x60860` | 58 | UnwindData |  |
| 73 | `JsPreventExtension` | `0x608A0` | 25 | UnwindData |  |
| 74 | `JsRelease` | `0x608C0` | 46 | UnwindData |  |
| 75 | `JsRunScript` | `0x60900` | 44 | UnwindData |  |
| 76 | `JsRunSerializedScript` | `0x60940` | 48 | UnwindData |  |
| 77 | `JsSerializeScript` | `0x60980` | 203 | UnwindData |  |
| 78 | `JsSetCurrentContext` | `0x60A60` | 25 | UnwindData |  |
| 79 | `JsSetException` | `0x60A80` | 25 | UnwindData |  |
| 80 | `JsSetExternalData` | `0x60AA0` | 46 | UnwindData |  |
| 81 | `JsSetIndexedProperty` | `0x60AE0` | 58 | UnwindData |  |
| 82 | `JsSetProperty` | `0x60B20` | 70 | UnwindData |  |
| 83 | `JsSetPrototype` | `0x60B70` | 46 | UnwindData |  |
| 84 | `JsSetRuntimeBeforeCollectCallback` | `0x60BB0` | 58 | UnwindData |  |
| 85 | `JsSetRuntimeMemoryAllocationCallback` | `0x60BF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `JsSetRuntimeMemoryLimit` | `0x60C30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `JsStartDebugging` | `0x60C60` | 25 | UnwindData |  |
| 88 | `JsStartProfiling` | `0x60C80` | 58 | UnwindData |  |
| 89 | `JsStopProfiling` | `0x60CC0` | 24 | UnwindData |  |
| 90 | `JsStrictEquals` | `0x60CE0` | 58 | UnwindData |  |
| 91 | `JsStringToPointer` | `0x60D20` | 58 | UnwindData |  |
| 92 | `JsValueToVariant` | `0x60D60` | 46 | UnwindData |  |
| 97 | `JsVariantToValue` | `0x60DA0` | 46 | UnwindData |  |
| 93 | `JsVarAddRef` | `0x83600` | 100 | UnwindData |  |
| 94 | `JsVarRelease` | `0x83670` | 80 | UnwindData |  |
| 95 | `JsVarToExtension` | `0x836D0` | 117 | UnwindData |  |
| 96 | `JsVarToScriptDirect` | `0x83750` | 94 | UnwindData |  |
