# Binary Specification: opencl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\opencl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9c0d8560191092a033bc4c662e6949881bbea8843d6abca1309d161561396448`
* **Total Exported Functions:** 123

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `clBuildProgram` | `0x4680` | 103 | UnwindData |  |
| 2 | `clCloneKernel` | `0x4740` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `clCompileProgram` | `0x47B0` | 174 | UnwindData |  |
| 4 | `clCreateBuffer` | `0x48E0` | 91 | UnwindData |  |
| 5 | `clCreateBufferWithProperties` | `0x4950` | 117 | UnwindData |  |
| 6 | `clCreateCommandQueue` | `0x4A80` | 61 | UnwindData |  |
| 7 | `clCreateCommandQueueWithProperties` | `0x4AD0` | 67 | UnwindData |  |
| 8 | `clCreateContext` | `0x4BA0` | 141 | UnwindData |  |
| 9 | `clCreateContextFromType` | `0x4C40` | 197 | UnwindData |  |
| 10 | `clCreateFromGLBuffer` | `0x5660` | 84 | UnwindData |  |
| 11 | `clCreateFromGLRenderbuffer` | `0x5710` | 84 | UnwindData |  |
| 12 | `clCreateFromGLTexture` | `0x57C0` | 138 | UnwindData |  |
| 13 | `clCreateFromGLTexture2D` | `0x5850` | 138 | UnwindData |  |
| 14 | `clCreateFromGLTexture3D` | `0x5950` | 138 | UnwindData |  |
| 15 | `clCreateImage` | `0x5AC0` | 117 | UnwindData |  |
| 16 | `clCreateImage2D` | `0x5B40` | 177 | UnwindData |  |
| 17 | `clCreateImage3D` | `0x5C80` | 218 | UnwindData |  |
| 18 | `clCreateImageWithProperties` | `0x5E00` | 155 | UnwindData |  |
| 19 | `clCreateKernel` | `0x5F80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `clCreateKernelsInProgram` | `0x5FF0` | 56 | UnwindData |  |
| 21 | `clCreatePipe` | `0x6060` | 117 | UnwindData |  |
| 22 | `clCreateProgramWithBinary` | `0x6140` | 155 | UnwindData |  |
| 23 | `clCreateProgramWithBuiltInKernels` | `0x6260` | 97 | UnwindData |  |
| 24 | `clCreateProgramWithIL` | `0x6320` | 67 | UnwindData |  |
| 25 | `clCreateProgramWithSource` | `0x63B0` | 97 | UnwindData |  |
| 26 | `clCreateSampler` | `0x6470` | 97 | UnwindData |  |
| 27 | `clCreateSamplerWithProperties` | `0x64E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `clCreateSubBuffer` | `0x65A0` | 97 | UnwindData |  |
| 29 | `clCreateSubDevices` | `0x6660` | 83 | UnwindData |  |
| 30 | `clCreateUserEvent` | `0x67C0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `clEnqueueAcquireGLObjects` | `0x6B70` | 115 | UnwindData |  |
| 32 | `clEnqueueBarrier` | `0x6C40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `clEnqueueBarrierWithWaitList` | `0x6C80` | 56 | UnwindData |  |
| 34 | `clEnqueueCopyBuffer` | `0x6D10` | 174 | UnwindData |  |
| 35 | `clEnqueueCopyBufferRect` | `0x6DD0` | 234 | UnwindData |  |
| 36 | `clEnqueueCopyBufferToImage` | `0x6F70` | 174 | UnwindData |  |
| 37 | `clEnqueueCopyImage` | `0x7110` | 174 | UnwindData |  |
| 38 | `clEnqueueCopyImageToBuffer` | `0x71D0` | 174 | UnwindData |  |
| 39 | `clEnqueueFillBuffer` | `0x7370` | 174 | UnwindData |  |
| 40 | `clEnqueueFillImage` | `0x74A0` | 161 | UnwindData |  |
| 41 | `clEnqueueMapBuffer` | `0x75C0` | 216 | UnwindData |  |
| 42 | `clEnqueueMapImage` | `0x7730` | 224 | UnwindData |  |
| 43 | `clEnqueueMarker` | `0x78D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `clEnqueueMarkerWithWaitList` | `0x7910` | 56 | UnwindData |  |
| 45 | `clEnqueueMigrateMemObjects` | `0x79A0` | 136 | UnwindData |  |
| 46 | `clEnqueueNDRangeKernel` | `0x7A80` | 174 | UnwindData |  |
| 47 | `clEnqueueNativeKernel` | `0x7BB0` | 197 | UnwindData |  |
| 48 | `clEnqueueReadBuffer` | `0x7D00` | 174 | UnwindData |  |
| 49 | `clEnqueueReadBufferRect` | `0x7DC0` | 266 | UnwindData |  |
| 50 | `clEnqueueReadImage` | `0x8000` | 203 | UnwindData |  |
| 51 | `clEnqueueReleaseGLObjects` | `0x84B0` | 115 | UnwindData |  |
| 52 | `clEnqueueSVMFree` | `0x8580` | 161 | UnwindData |  |
| 53 | `clEnqueueSVMMap` | `0x86A0` | 161 | UnwindData |  |
| 54 | `clEnqueueSVMMemFill` | `0x87C0` | 161 | UnwindData |  |
| 55 | `clEnqueueSVMMemcpy` | `0x88E0` | 161 | UnwindData |  |
| 56 | `clEnqueueSVMMigrateMem` | `0x8A00` | 161 | UnwindData |  |
| 57 | `clEnqueueSVMUnmap` | `0x8B20` | 83 | UnwindData |  |
| 58 | `clEnqueueTask` | `0x8BC0` | 83 | UnwindData |  |
| 59 | `clEnqueueUnmapMemObject` | `0x8C60` | 103 | UnwindData |  |
| 60 | `clEnqueueWaitForEvents` | `0x8D20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `clEnqueueWriteBuffer` | `0x8D80` | 174 | UnwindData |  |
| 62 | `clEnqueueWriteBufferRect` | `0x8E40` | 266 | UnwindData |  |
| 63 | `clEnqueueWriteImage` | `0x9080` | 203 | UnwindData |  |
| 64 | `clFinish` | `0x91F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `clFlush` | `0x9250` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `clGetCommandQueueInfo` | `0x92B0` | 77 | UnwindData |  |
| 67 | `clGetContextInfo` | `0x9350` | 77 | UnwindData |  |
| 68 | `clGetDeviceAndHostTimer` | `0x93F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `clGetDeviceIDs` | `0x9450` | 77 | UnwindData |  |
| 70 | `clGetDeviceInfo` | `0x9820` | 77 | UnwindData |  |
| 71 | `clGetEventInfo` | `0x98C0` | 83 | UnwindData |  |
| 72 | `clGetEventProfilingInfo` | `0x9960` | 83 | UnwindData |  |
| 75 | `clGetGLObjectInfo` | `0x9B00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `clGetGLTextureInfo` | `0x9B70` | 95 | UnwindData |  |
| 77 | `clGetHostTimer` | `0x9C30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `clGetImageInfo` | `0x9C90` | 83 | UnwindData |  |
| 79 | `clGetKernelArgInfo` | `0x9D30` | 103 | UnwindData |  |
| 80 | `clGetKernelInfo` | `0x9DF0` | 83 | UnwindData |  |
| 81 | `clGetKernelSubGroupInfo` | `0x9E90` | 163 | UnwindData |  |
| 82 | `clGetKernelWorkGroupInfo` | `0xA0E0` | 103 | UnwindData |  |
| 83 | `clGetMemObjectInfo` | `0xA1A0` | 83 | UnwindData |  |
| 84 | `clGetPipeInfo` | `0xA240` | 83 | UnwindData |  |
| 86 | `clGetPlatformInfo` | `0xA2E0` | 77 | UnwindData |  |
| 87 | `clGetProgramBuildInfo` | `0xA380` | 103 | UnwindData |  |
| 88 | `clGetProgramInfo` | `0xA440` | 83 | UnwindData |  |
| 89 | `clGetSamplerInfo` | `0xA4E0` | 83 | UnwindData |  |
| 90 | `clGetSupportedImageFormats` | `0xA580` | 103 | UnwindData |  |
| 91 | `clLinkProgram` | `0xA640` | 191 | UnwindData |  |
| 92 | `clReleaseCommandQueue` | `0xA790` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `clReleaseContext` | `0xA7E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `clReleaseDevice` | `0xA830` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `clReleaseEvent` | `0xA900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `clReleaseKernel` | `0xA960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `clReleaseMemObject` | `0xA9C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `clReleaseProgram` | `0xAA20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `clReleaseSampler` | `0xAA80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `clRetainCommandQueue` | `0xAAE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `clRetainContext` | `0xAB30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `clRetainDevice` | `0xAB80` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `clRetainEvent` | `0xAC50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `clRetainKernel` | `0xACB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `clRetainMemObject` | `0xAD10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `clRetainProgram` | `0xAD70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `clRetainSampler` | `0xADD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `clSVMAlloc` | `0xAE30` | 55 | UnwindData |  |
| 109 | `clSVMFree` | `0xAEA0` | 51 | UnwindData |  |
| 110 | `clSetCommandQueueProperty` | `0xAF10` | 50 | UnwindData |  |
| 111 | `clSetContextDestructorCallback` | `0xAF80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `clSetDefaultDeviceCommandQueue` | `0xAFE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `clSetEventCallback` | `0xB040` | 56 | UnwindData |  |
| 114 | `clSetKernelArg` | `0xB0B0` | 56 | UnwindData |  |
| 115 | `clSetKernelArgSVMPointer` | `0xB0F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `clSetKernelExecInfo` | `0xB180` | 56 | UnwindData |  |
| 117 | `clSetMemObjectDestructorCallback` | `0xB1F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `clSetProgramReleaseCallback` | `0xB250` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `clSetProgramSpecializationConstant` | `0xB2B0` | 56 | UnwindData |  |
| 120 | `clSetUserEventStatus` | `0xB320` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `clUnloadCompiler` | `0xB380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `clUnloadPlatformCompiler` | `0xB3B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `clWaitForEvents` | `0xB410` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `clGetExtensionFunctionAddress` | `0xB4A0` | 83 | UnwindData |  |
| 74 | `clGetExtensionFunctionAddressForPlatform` | `0xB500` | 154 | UnwindData |  |
| 85 | `clGetPlatformIDs` | `0xB750` | 232 | UnwindData |  |
