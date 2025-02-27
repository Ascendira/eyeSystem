import json
from datetime import datetime

from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from patientInfo.models import BaseInfo as mBaseInfo
from patientInfo.models import EyeParameter

# Create your views here.
def index(request):
    return render(request, "index.html")

response_template = {
    "success": True,
    "errCode": 200,
    "data": {
    }
}

class BaseInfo(View):
    def get(self, request, pageNum, pageSize):
        data = mBaseInfo.objects.all().order_by('-screen_date').values()
        data = list(data)
        length = len(data)
        l = pageNum * pageSize
        r = l + pageSize
        if l > len(data):
            return JsonResponse({'data': []})
        elif r >= len(data):
            data = data[l:len(data)]
        else:
            data = data[l:r]
        response = {
            'success': True,
            'errCode': 0,
            'total': length,
            'data': data
        }
        return JsonResponse(response)

class PatientInfoView(View):
    def post(self, request, date):
        try:
            naive_date = datetime.strptime(date, "%Y-%m-%d-%H-%M-%S")
            screen_date = timezone.make_aware(naive_date)
        except ValueError:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'Date Format Error'}, status=400)

        try:
            data = json.loads(request.body)['data']
            patient_id = data['patient_id']
            obj, created = mBaseInfo.objects.update_or_create(
                patient_id=patient_id,
                defaults={
                    'phone_number': data['phone_number'],
                    'name': data['name'],
                    'gender': data['gender'],
                    'age': data['age'],
                    'nation': data['nation'],
                    'habitation': data['habitation'],
                    'school': data['school'],
                    'grade': data['grade'],
                    'screen_date': screen_date,
                    'glasses_worn_type': data['glasses_worn_type'],
                    'other_glasses_worn_type': data['other_glasses_worn_type'],
                }
            )

            obj.full_clean()
            obj.save()

            data = data['eyeParameter']
            obj, created = EyeParameter.objects.update_or_create(
                patient_id=patient_id,
                defaults={
                    'vision_Sc_right': data['vision_Sc_right'],  # 右眼裸眼视力
                    'vision_Sc_left': data['vision_Sc_left'],  # 左眼裸眼视力
                    'vision_Cc_right': data['vision_Cc_right'],  # 右眼戴镜视力
                    'vision_Cc_left': data['vision_Cc_left'],  # 左眼戴镜视力
                    'intraocular_pressure_right': data['intraocular_pressure_right'],  # 右眼眼压
                    'intraocular_pressure_left': data['intraocular_pressure_left'],  # 左眼眼压
                    'computer_optometry_S_right': data['computer_optometry_S_right'],  # 球镜电脑验光结果右眼
                    'computer_optometry_S_left': data['computer_optometry_S_left'],  # 球镜电脑验光结果左眼
                    'computer_optometry_C_right': data['computer_optometry_C_right'],  # 柱镜电脑验光结果右眼
                    'computer_optometry_C_left': data['computer_optometry_C_left'],  # 柱镜电脑验光结果左眼
                    'computer_optometry_A_right': data['computer_optometry_A_right'],  # 轴位电脑验光结果右眼
                    'computer_optometry_A_left': data['computer_optometry_A_left'],  # 轴位电脑验光结果左眼
                    'corneal_curvature_A': data['corneal_curvature_A'],  # 角膜曲率右眼R1A
                    'corneal_curvature_C': data['corneal_curvature_C'],  # 角膜曲率左眼R1C
                    'corneal_curvature_E': data['corneal_curvature_E'],  # 角膜曲率右眼R2E
                    'corneal_curvature_G': data['corneal_curvature_G'],  # 角膜曲率左眼R2G
                    'corneal_curvature_B': data['corneal_curvature_B'],  # 角膜曲率右眼R1B
                    'corneal_curvature_D': data['corneal_curvature_D'],  # 角膜曲率左眼R1D
                    'corneal_curvature_F': data['corneal_curvature_F'],  # 角膜曲率右眼R2F
                    'corneal_curvature_H': data['corneal_curvature_H'],  # 角膜曲率左眼R2H
                    'screen_optometry_S_right': data['screen_optometry_S_right'],  # 球镜筛查仪验光结果右眼
                    'screen_optometry_S_left': data['screen_optometry_S_left'],  # 球镜筛查仪验光结果左眼
                    'screen_optometry_C_right': data['screen_optometry_C_right'],  # 柱镜筛查仪验光结果右眼
                    'screen_optometry_C_left': data['screen_optometry_C_left'],  # 柱镜筛查仪验光结果左眼
                    'screen_optometry_A_right': data['screen_optometry_A_right'],  # 轴位筛查仪验光结果右眼
                    'screen_optometry_A_left': data['screen_optometry_A_left'],  # 轴位筛查仪验光结果左眼
                    'AL_right': data['AL_right'],  # 右眼眼轴长度
                    'AL_left': data['AL_left'],  # 左眼眼轴长度
                    'CCT_right': data['CCT_right'],  # 右眼中心角膜厚度
                    'CCT_left': data['CCT_left'],  # 左眼中心角膜厚度
                    'ACD_right': data['ACD_right'],  # 右眼前房深度
                    'ACD_left': data['ACD_left'],  # 左眼前房深度
                    'LT_right': data['LT_right'],  # 右眼晶体厚度
                    'LT_left': data['LT_left'],  # 左眼晶体厚度
                    'VCD_right': data['VCD_right'],  # 右眼玻璃体腔长度
                    'VCD_left': data['VCD_left'],  # 左眼玻璃体腔长度
                    'PD_right': data['PD_right'],  # 右眼瞳孔直径
                    'PD_left': data['PD_left'],  # 左眼瞳孔直径
                    'WTW_right': data['WTW_right'],  # 右眼角膜直径
                    'WTW_left': data['WTW_left'],  # 左眼角膜直径
                    'refractive_SE_right': data['refractive_SE_right'],  # 右眼屈光参数SE
                    'refractive_SE_left': data['refractive_SE_left'],  # 左眼屈光参数SE
                    'refractive_A': data['refractive_A'],  # 屈光参数右眼R1A
                    'refractive_C': data['refractive_C'],  # 屈光参数左眼R1C
                    'refractive_E': data['refractive_E'],  # 屈光参数右眼R2E
                    'refractive_G': data['refractive_G'],  # 屈光参数左眼R2G
                    'refractive_I': data['refractive_I'],  # 屈光参数右眼K1I
                    'refractive_K': data['refractive_K'],  # 屈光参数左眼K1K
                    'refractive_M': data['refractive_M'],  # 屈光参数右眼K2M
                    'refractive_O': data['refractive_O'],  # 屈光参数左眼K2O
                    'refractive_B': data['refractive_B'],  # 屈光参数右眼R1B
                    'refractive_D': data['refractive_D'],  # 屈光参数左眼R1D
                    'refractive_F': data['refractive_F'],  # 屈光参数右眼R2F
                    'refractive_H': data['refractive_H'],  # 屈光参数左眼R2H
                    'refractive_J': data['refractive_J'],  # 屈光参数右眼K1J
                    'refractive_L': data['refractive_L'],  # 屈光参数左眼K1L
                    'refractive_N': data['refractive_N'],  # 屈光参数右眼K2N
                    'refractive_P': data['refractive_P'],  # 屈光参数左眼K2P
                    'correcting_intraocular_pressure_right': data['correcting_intraocular_pressure_right'],  # 右眼矫正眼压
                    'correcting_intraocular_pressure_left': data['correcting_intraocular_pressure_left'],  # 左眼矫正眼压
                    'thinnest_center_thickness_right': data['thinnest_center_thickness_right'],  # 右眼角膜中央最薄点厚度
                    'thinnest_center_thickness_left': data['thinnest_center_thickness_left'],  # 左眼角膜中央最薄点厚度
                    'DA_ratio_one_right': data['DA_ratio_one_right'],  # 右眼1mm角膜定点形变幅度的比值
                    'DA_ratio_one_left': data['DA_ratio_one_left'],  # 左眼1mm角膜定点形变幅度的比值
                    'DA_ratio_two_right': data['DA_ratio_two_right'],  # 右眼2mm角膜定点形变幅度的比值
                    'DA_ratio_two_left': data['DA_ratio_two_left'],  # 左眼2mm角膜定点形变幅度的比值
                    'ARTh_right': data['ARTh_right'],  # 右眼厚度变化率
                    'ARTh_left': data['ARTh_left'],  # 左眼厚度变化率
                    'IR_right': data['IR_right'],  # 右眼综合半径
                    'IR_left': data['IR_left'],  # 左眼综合半径
                    'SP_A1_right': data['SP_A1_right'],  # 右眼角膜硬度参数
                    'SP_A1_left': data['SP_A1_left'],  # 左眼角膜硬度参数
                    'CBI_right': data['CBI_right'],  # 右眼生物力学参数
                    'CBI_left': data['CBI_left'],  # 左眼生物力学参数
                    'SSI_right': data['SSI_right'],  # 右眼应力应变参数
                    'SSI_left': data['SSI_left'],  # 左眼应力应变参数
                }
            )

            obj.full_clean()
            obj.save()

            return JsonResponse(response_template)

        except ValidationError as e:
            error_dict = {field: list(errors) for field, errors in e.message_dict.items()}
            return JsonResponse({'status': 'error', 'message': '验证失败', 'errors': error_dict}, status=400)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    def get(self, request, patient_id):
        # 判断是查询全部病人信息还是查询基础信息
        if 'base' in request.path:
            return self.get_base_info(request, patient_id)
        else:
            return self.get_all_info(request, patient_id)

    def get_all_info(self, request, patient_id):
        # 查询全部病人信息
        info = mBaseInfo.objects.filter(patient_id=patient_id).values()
        if not info:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'No Patient Found'}, status=400)
        info = list(info)[0]

        eye_parameter = list(EyeParameter.objects.filter(patient_id=patient_id).values())
        info['eyeParameter'] = eye_parameter

        response = response_template.copy()
        response['data'] = info
        return JsonResponse(response)

    def get_base_info(self, request, patient_id):
        # 查询基础信息
        base_info = mBaseInfo.objects.filter(patient_id=patient_id).values()
        if not base_info:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'No Patient Found'}, status=400)

        response = response_template.copy()
        response['data'] = list(base_info)[0]
        return JsonResponse(response)

    def delete(self, request, patient_id):
        # 删除该病人信息
        try:
            mBaseInfo.objects.filter(patient_id=patient_id).delete()
            EyeParameter.objects.filter(patient_id=patient_id).delete()
        except Exception as e:
            return JsonResponse({'success': False, 'errCode': 500, 'message': str(e)}, status=500)

        return JsonResponse(response_template)