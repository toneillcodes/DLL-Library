# Binary Specification: jscript9.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\jscript9.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea39b84abd6af91073a4d212a9dd114228e8d75c2402e6390fdaa4dfd8f1de18`
* **Total Exported Functions:** 97

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 95 | `JsVarToExtension` | `0x149F90` | 117 | UnwindData |  |
| 94 | `JsVarRelease` | `0x150360` | 372 | UnwindData |  |
| 93 | `JsVarAddRef` | `0x150AE0` | 168 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x19B890` | 361 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1E2E90` | 226 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1E30F0` | 177 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1E31B0` | 175 | UnwindData |  |
| 5 | `JsAddRef` | `0x1F7720` | 46 | UnwindData |  |
| 6 | `JsBoolToBoolean` | `0x1F7760` | 46 | UnwindData |  |
| 7 | `JsBooleanToBool` | `0x1F77A0` | 46 | UnwindData |  |
| 8 | `JsCallFunction` | `0x1F77E0` | 71 | UnwindData |  |
| 9 | `JsCollectGarbage` | `0x1F7830` | 25 | UnwindData |  |
| 10 | `JsConstructObject` | `0x1F7850` | 71 | UnwindData |  |
| 11 | `JsConvertValueToBoolean` | `0x1F78A0` | 46 | UnwindData |  |
| 12 | `JsConvertValueToNumber` | `0x1F78E0` | 46 | UnwindData |  |
| 13 | `JsConvertValueToObject` | `0x1F7920` | 46 | UnwindData |  |
| 14 | `JsConvertValueToString` | `0x1F7960` | 46 | UnwindData |  |
| 15 | `JsCreateArray` | `0x1F79A0` | 46 | UnwindData |  |
| 16 | `JsCreateContext` | `0x1F79E0` | 58 | UnwindData |  |
| 17 | `JsCreateError` | `0x1F7A20` | 46 | UnwindData |  |
| 18 | `JsCreateExternalObject` | `0x1F7A60` | 58 | UnwindData |  |
| 19 | `JsCreateExternalType` | `0x1F7AA0` | 46 | UnwindData |  |
| 20 | `JsCreateFunction` | `0x1F7AE0` | 58 | UnwindData |  |
| 21 | `JsCreateObject` | `0x1F7B20` | 25 | UnwindData |  |
| 22 | `JsCreateRangeError` | `0x1F7B40` | 46 | UnwindData |  |
| 23 | `JsCreateReferenceError` | `0x1F7B80` | 46 | UnwindData |  |
| 24 | `JsCreateRuntime` | `0x1F7BC0` | 70 | UnwindData |  |
| 25 | `JsCreateSyntaxError` | `0x1F7C10` | 46 | UnwindData |  |
| 26 | `JsCreateTypeError` | `0x1F7C50` | 46 | UnwindData |  |
| 27 | `JsCreateTypedExternalObject` | `0x1F7C90` | 58 | UnwindData |  |
| 28 | `JsCreateURIError` | `0x1F7CD0` | 46 | UnwindData |  |
| 29 | `JsDefineProperty` | `0x1F7D10` | 70 | UnwindData |  |
| 30 | `JsDeleteIndexedProperty` | `0x1F7D60` | 46 | UnwindData |  |
| 31 | `JsDeleteProperty` | `0x1F7DA0` | 70 | UnwindData |  |
| 32 | `JsDisableRuntimeExecution` | `0x1F7DF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `JsDisposeRuntime` | `0x1F7E50` | 25 | UnwindData |  |
| 34 | `JsDoubleToNumber` | `0x1F7E70` | 48 | UnwindData |  |
| 35 | `JsEnableRuntimeExecution` | `0x1F7EB0` | 25 | UnwindData |  |
| 36 | `JsEnumerateHeap` | `0x1F7ED0` | 112 | UnwindData |  |
| 37 | `JsEquals` | `0x1F7F50` | 58 | UnwindData |  |
| 38 | `JsGetAndClearException` | `0x1F7F90` | 192 | UnwindData |  |
| 39 | `JsGetCurrentContext` | `0x1F8060` | 57 | UnwindData |  |
| 40 | `JsGetDefaultTypeDescription` | `0x1F80A0` | 25 | UnwindData |  |
| 41 | `JsGetExtensionAllowed` | `0x1F80C0` | 46 | UnwindData |  |
| 42 | `JsGetExternalData` | `0x1F8100` | 46 | UnwindData |  |
| 43 | `JsGetExternalType` | `0x1F8140` | 46 | UnwindData |  |
| 44 | `JsGetFalseValue` | `0x1F8180` | 25 | UnwindData |  |
| 45 | `JsGetGlobalObject` | `0x1F81A0` | 25 | UnwindData |  |
| 46 | `JsGetIndexedProperty` | `0x1F81C0` | 58 | UnwindData |  |
| 47 | `JsGetNullValue` | `0x1F8200` | 25 | UnwindData |  |
| 48 | `JsGetOwnPropertyDescriptor` | `0x1F8220` | 58 | UnwindData |  |
| 49 | `JsGetOwnPropertyNames` | `0x1F8260` | 46 | UnwindData |  |
| 50 | `JsGetProperty` | `0x1F82A0` | 58 | UnwindData |  |
| 51 | `JsGetPropertyIdFromName` | `0x1F82E0` | 46 | UnwindData |  |
| 52 | `JsGetPropertyNameFromId` | `0x1F8320` | 46 | UnwindData |  |
| 53 | `JsGetPrototype` | `0x1F8360` | 46 | UnwindData |  |
| 54 | `JsGetRuntime` | `0x1F83A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `JsGetRuntimeMemoryLimit` | `0x1F83F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `JsGetRuntimeMemoryUsage` | `0x1F8430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `JsGetStringLength` | `0x1F8470` | 46 | UnwindData |  |
| 58 | `JsGetTrueValue` | `0x1F84B0` | 25 | UnwindData |  |
| 59 | `JsGetUndefinedValue` | `0x1F84D0` | 25 | UnwindData |  |
| 60 | `JsGetValueType` | `0x1F84F0` | 46 | UnwindData |  |
| 61 | `JsHasException` | `0x1F8530` | 165 | UnwindData |  |
| 62 | `JsHasExternalData` | `0x1F85E0` | 46 | UnwindData |  |
| 63 | `JsHasIndexedProperty` | `0x1F8620` | 58 | UnwindData |  |
| 64 | `JsHasProperty` | `0x1F8660` | 58 | UnwindData |  |
| 65 | `JsIdle` | `0x1F86A0` | 25 | UnwindData |  |
| 66 | `JsIntToNumber` | `0x1F86C0` | 46 | UnwindData |  |
| 67 | `JsIsEnumeratingHeap` | `0x1F8700` | 89 | UnwindData |  |
| 68 | `JsIsRuntimeExecutionDisabled` | `0x1F8760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `JsNumberToDouble` | `0x1F87A0` | 46 | UnwindData |  |
| 70 | `JsParseScript` | `0x1F87E0` | 44 | UnwindData |  |
| 71 | `JsParseSerializedScript` | `0x1F8820` | 48 | UnwindData |  |
| 72 | `JsPointerToString` | `0x1F8860` | 58 | UnwindData |  |
| 73 | `JsPreventExtension` | `0x1F88A0` | 25 | UnwindData |  |
| 74 | `JsRelease` | `0x1F88C0` | 46 | UnwindData |  |
| 75 | `JsRunScript` | `0x1F8900` | 44 | UnwindData |  |
| 76 | `JsRunSerializedScript` | `0x1F8940` | 48 | UnwindData |  |
| 77 | `JsSerializeScript` | `0x1F8980` | 203 | UnwindData |  |
| 78 | `JsSetCurrentContext` | `0x1F8A60` | 25 | UnwindData |  |
| 79 | `JsSetException` | `0x1F8A80` | 25 | UnwindData |  |
| 80 | `JsSetExternalData` | `0x1F8AA0` | 46 | UnwindData |  |
| 81 | `JsSetIndexedProperty` | `0x1F8AE0` | 58 | UnwindData |  |
| 82 | `JsSetProperty` | `0x1F8B20` | 70 | UnwindData |  |
| 83 | `JsSetPrototype` | `0x1F8B70` | 46 | UnwindData |  |
| 84 | `JsSetRuntimeBeforeCollectCallback` | `0x1F8BB0` | 58 | UnwindData |  |
| 85 | `JsSetRuntimeMemoryAllocationCallback` | `0x1F8BF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `JsSetRuntimeMemoryLimit` | `0x1F8C30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `JsStartDebugging` | `0x1F8C60` | 25 | UnwindData |  |
| 88 | `JsStartProfiling` | `0x1F8C80` | 58 | UnwindData |  |
| 89 | `JsStopProfiling` | `0x1F8CC0` | 24 | UnwindData |  |
| 90 | `JsStrictEquals` | `0x1F8CE0` | 58 | UnwindData |  |
| 91 | `JsStringToPointer` | `0x1F8D20` | 58 | UnwindData |  |
| 92 | `JsValueToVariant` | `0x1F8D60` | 46 | UnwindData |  |
| 97 | `JsVariantToValue` | `0x1F8DA0` | 46 | UnwindData |  |
| 96 | `JsVarToScriptDirect` | `0x211710` | 94 | UnwindData |  |
