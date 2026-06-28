# Binary Specification: jscript9.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\jscript9.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cf62cf1650f9ea9bad99da313730f739717d41f61b6cb32097fe6068ca45f5d`
* **Total Exported Functions:** 97

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 95 | `JsVarToExtension` | `0x1494E0` | 117 | UnwindData |  |
| 94 | `JsVarRelease` | `0x14F8B0` | 372 | UnwindData |  |
| 93 | `JsVarAddRef` | `0x150030` | 168 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x19B7D0` | 361 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1E4830` | 226 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1E4A90` | 177 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1E4B50` | 175 | UnwindData |  |
| 5 | `JsAddRef` | `0x1F8BF0` | 46 | UnwindData |  |
| 6 | `JsBoolToBoolean` | `0x1F8C30` | 46 | UnwindData |  |
| 7 | `JsBooleanToBool` | `0x1F8C70` | 46 | UnwindData |  |
| 8 | `JsCallFunction` | `0x1F8CB0` | 71 | UnwindData |  |
| 9 | `JsCollectGarbage` | `0x1F8D00` | 25 | UnwindData |  |
| 10 | `JsConstructObject` | `0x1F8D20` | 71 | UnwindData |  |
| 11 | `JsConvertValueToBoolean` | `0x1F8D70` | 46 | UnwindData |  |
| 12 | `JsConvertValueToNumber` | `0x1F8DB0` | 46 | UnwindData |  |
| 13 | `JsConvertValueToObject` | `0x1F8DF0` | 46 | UnwindData |  |
| 14 | `JsConvertValueToString` | `0x1F8E30` | 46 | UnwindData |  |
| 15 | `JsCreateArray` | `0x1F8E70` | 46 | UnwindData |  |
| 16 | `JsCreateContext` | `0x1F8EB0` | 58 | UnwindData |  |
| 17 | `JsCreateError` | `0x1F8EF0` | 46 | UnwindData |  |
| 18 | `JsCreateExternalObject` | `0x1F8F30` | 58 | UnwindData |  |
| 19 | `JsCreateExternalType` | `0x1F8F70` | 46 | UnwindData |  |
| 20 | `JsCreateFunction` | `0x1F8FB0` | 58 | UnwindData |  |
| 21 | `JsCreateObject` | `0x1F8FF0` | 25 | UnwindData |  |
| 22 | `JsCreateRangeError` | `0x1F9010` | 46 | UnwindData |  |
| 23 | `JsCreateReferenceError` | `0x1F9050` | 46 | UnwindData |  |
| 24 | `JsCreateRuntime` | `0x1F9090` | 70 | UnwindData |  |
| 25 | `JsCreateSyntaxError` | `0x1F90E0` | 46 | UnwindData |  |
| 26 | `JsCreateTypeError` | `0x1F9120` | 46 | UnwindData |  |
| 27 | `JsCreateTypedExternalObject` | `0x1F9160` | 58 | UnwindData |  |
| 28 | `JsCreateURIError` | `0x1F91A0` | 46 | UnwindData |  |
| 29 | `JsDefineProperty` | `0x1F91E0` | 70 | UnwindData |  |
| 30 | `JsDeleteIndexedProperty` | `0x1F9230` | 46 | UnwindData |  |
| 31 | `JsDeleteProperty` | `0x1F9270` | 70 | UnwindData |  |
| 32 | `JsDisableRuntimeExecution` | `0x1F92C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `JsDisposeRuntime` | `0x1F9320` | 25 | UnwindData |  |
| 34 | `JsDoubleToNumber` | `0x1F9340` | 48 | UnwindData |  |
| 35 | `JsEnableRuntimeExecution` | `0x1F9380` | 25 | UnwindData |  |
| 36 | `JsEnumerateHeap` | `0x1F93A0` | 112 | UnwindData |  |
| 37 | `JsEquals` | `0x1F9420` | 58 | UnwindData |  |
| 38 | `JsGetAndClearException` | `0x1F9460` | 192 | UnwindData |  |
| 39 | `JsGetCurrentContext` | `0x1F9530` | 57 | UnwindData |  |
| 40 | `JsGetDefaultTypeDescription` | `0x1F9570` | 25 | UnwindData |  |
| 41 | `JsGetExtensionAllowed` | `0x1F9590` | 46 | UnwindData |  |
| 42 | `JsGetExternalData` | `0x1F95D0` | 46 | UnwindData |  |
| 43 | `JsGetExternalType` | `0x1F9610` | 46 | UnwindData |  |
| 44 | `JsGetFalseValue` | `0x1F9650` | 25 | UnwindData |  |
| 45 | `JsGetGlobalObject` | `0x1F9670` | 25 | UnwindData |  |
| 46 | `JsGetIndexedProperty` | `0x1F9690` | 58 | UnwindData |  |
| 47 | `JsGetNullValue` | `0x1F96D0` | 25 | UnwindData |  |
| 48 | `JsGetOwnPropertyDescriptor` | `0x1F96F0` | 58 | UnwindData |  |
| 49 | `JsGetOwnPropertyNames` | `0x1F9730` | 46 | UnwindData |  |
| 50 | `JsGetProperty` | `0x1F9770` | 58 | UnwindData |  |
| 51 | `JsGetPropertyIdFromName` | `0x1F97B0` | 46 | UnwindData |  |
| 52 | `JsGetPropertyNameFromId` | `0x1F97F0` | 46 | UnwindData |  |
| 53 | `JsGetPrototype` | `0x1F9830` | 46 | UnwindData |  |
| 54 | `JsGetRuntime` | `0x1F9870` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `JsGetRuntimeMemoryLimit` | `0x1F98C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `JsGetRuntimeMemoryUsage` | `0x1F9900` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `JsGetStringLength` | `0x1F9940` | 46 | UnwindData |  |
| 58 | `JsGetTrueValue` | `0x1F9980` | 25 | UnwindData |  |
| 59 | `JsGetUndefinedValue` | `0x1F99A0` | 25 | UnwindData |  |
| 60 | `JsGetValueType` | `0x1F99C0` | 46 | UnwindData |  |
| 61 | `JsHasException` | `0x1F9A00` | 165 | UnwindData |  |
| 62 | `JsHasExternalData` | `0x1F9AB0` | 46 | UnwindData |  |
| 63 | `JsHasIndexedProperty` | `0x1F9AF0` | 58 | UnwindData |  |
| 64 | `JsHasProperty` | `0x1F9B30` | 58 | UnwindData |  |
| 65 | `JsIdle` | `0x1F9B70` | 25 | UnwindData |  |
| 66 | `JsIntToNumber` | `0x1F9B90` | 46 | UnwindData |  |
| 67 | `JsIsEnumeratingHeap` | `0x1F9BD0` | 89 | UnwindData |  |
| 68 | `JsIsRuntimeExecutionDisabled` | `0x1F9C30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `JsNumberToDouble` | `0x1F9C70` | 46 | UnwindData |  |
| 70 | `JsParseScript` | `0x1F9CB0` | 44 | UnwindData |  |
| 71 | `JsParseSerializedScript` | `0x1F9CF0` | 48 | UnwindData |  |
| 72 | `JsPointerToString` | `0x1F9D30` | 58 | UnwindData |  |
| 73 | `JsPreventExtension` | `0x1F9D70` | 25 | UnwindData |  |
| 74 | `JsRelease` | `0x1F9D90` | 46 | UnwindData |  |
| 75 | `JsRunScript` | `0x1F9DD0` | 44 | UnwindData |  |
| 76 | `JsRunSerializedScript` | `0x1F9E10` | 48 | UnwindData |  |
| 77 | `JsSerializeScript` | `0x1F9E50` | 203 | UnwindData |  |
| 78 | `JsSetCurrentContext` | `0x1F9F30` | 25 | UnwindData |  |
| 79 | `JsSetException` | `0x1F9F50` | 25 | UnwindData |  |
| 80 | `JsSetExternalData` | `0x1F9F70` | 46 | UnwindData |  |
| 81 | `JsSetIndexedProperty` | `0x1F9FB0` | 58 | UnwindData |  |
| 82 | `JsSetProperty` | `0x1F9FF0` | 70 | UnwindData |  |
| 83 | `JsSetPrototype` | `0x1FA040` | 46 | UnwindData |  |
| 84 | `JsSetRuntimeBeforeCollectCallback` | `0x1FA080` | 58 | UnwindData |  |
| 85 | `JsSetRuntimeMemoryAllocationCallback` | `0x1FA0C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `JsSetRuntimeMemoryLimit` | `0x1FA100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `JsStartDebugging` | `0x1FA130` | 25 | UnwindData |  |
| 88 | `JsStartProfiling` | `0x1FA150` | 58 | UnwindData |  |
| 89 | `JsStopProfiling` | `0x1FA190` | 24 | UnwindData |  |
| 90 | `JsStrictEquals` | `0x1FA1B0` | 58 | UnwindData |  |
| 91 | `JsStringToPointer` | `0x1FA1F0` | 58 | UnwindData |  |
| 92 | `JsValueToVariant` | `0x1FA230` | 46 | UnwindData |  |
| 97 | `JsVariantToValue` | `0x1FA270` | 46 | UnwindData |  |
| 96 | `JsVarToScriptDirect` | `0x211DB0` | 94 | UnwindData |  |
