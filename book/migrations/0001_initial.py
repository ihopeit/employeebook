# Generated by Django 3.2 on 2021-04-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='工号')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='姓名')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='邮件')),
                ('status', models.CharField(blank=True, choices=[('在职', '在职'), ('辞职', '辞职'), ('辞退', '辞退'), ('自离', '自离')], max_length=100, null=True, verbose_name='人员状态')),
                ('emptype', models.CharField(blank=True, choices=[('正式员工', '正式员工'), ('实习生', '实习生'), ('兼职', '兼职'), ('其他', '其他')], max_length=100, null=True, verbose_name='人员类别')),
                ('contract_corp', models.CharField(blank=True, max_length=100, null=True, verbose_name='合同签约分公司')),
                ('office_city', models.CharField(blank=True, max_length=100, null=True, verbose_name='办公区域')),
                ('dept1', models.CharField(blank=True, choices=[('运营部', '运营部'), ('技术部', '技术部'), ('人事行政部部', '人事行政部部'), ('客服部', '客服部'), ('财务部', '财务部')], max_length=100, null=True, verbose_name='部门1')),
                ('dept2', models.CharField(blank=True, choices=[('运营部', '运营部'), ('技术部', '技术部'), ('人事行政部部', '人事行政部部'), ('客服部', '客服部'), ('财务部', '财务部')], max_length=100, null=True, verbose_name='部门2')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='岗位名称')),
                ('enroll_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='入职日期')),
                ('identity', models.CharField(blank=True, max_length=100, null=True, verbose_name='身份证号')),
                ('bankcardno', models.CharField(blank=True, max_length=100, null=True, verbose_name='工商银行卡号')),
                ('card_creation_bank', models.CharField(blank=True, max_length=100, null=True, verbose_name='开户行')),
                ('gender', models.CharField(blank=True, choices=[('男', '男'), ('女', '女'), ('其他', '其他')], max_length=100, null=True, verbose_name='性别')),
                ('nation', models.CharField(blank=True, max_length=100, null=True, verbose_name='民族')),
                ('native_place', models.CharField(blank=True, max_length=100, null=True, verbose_name='籍贯')),
                ('birth_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='出生日期')),
                ('edu_degree', models.CharField(blank=True, max_length=100, null=True, verbose_name='学历')),
                ('edu_school', models.CharField(blank=True, max_length=100, null=True, verbose_name='毕业院校')),
                ('edu_major', models.CharField(blank=True, max_length=100, null=True, verbose_name='专业')),
                ('edu_graduate_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='毕业日期')),
                ('huji_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='户籍类型')),
                ('insured_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='参保类型')),
                ('huji_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='户籍地址')),
                ('resident_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='现住址')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True, verbose_name='手机')),
                ('wechat', models.CharField(blank=True, max_length=100, null=True, verbose_name='wechat')),
                ('urgent_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='紧急联系人')),
                ('urgent_relation', models.CharField(blank=True, max_length=100, null=True, verbose_name='与本人关系')),
                ('urgent_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='紧急联系人电话')),
                ('created_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='数据录入时间')),
                ('updated_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='数据更新时间')),
                ('comment', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '花名册',
            },
        ),
    ]
